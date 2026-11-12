import sqlmodel
from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import Session, select
from db import get_session
from models import Item,ItemCreate,ItemResponse
from fastapi.responses import RedirectResponse

from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import SQLModel
from db import engine
import models  # CRITICAL: Must be imported so SQLModel registers your table=True classes


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs once when FastAPI starts up: creates all missing tables & sequences
    SQLModel.metadata.create_all(engine)
    yield
    # Optional cleanup code when FastAPI shuts down


app = FastAPI(lifespan=lifespan)


@app.get("/")
def home():
    return RedirectResponse(url="/docs")

@app.post("/items",response_model=ItemResponse,status_code=status.HTTP_201_CREATED)
def create_or_update_item(item:ItemCreate, session:Session = Depends(get_session)):
    if session.exec(select(Item).where(Item.name==item.name)).first():
        raise HTTPException(status_code=400,detail="Item already exists")
    db_item = Item.model_validate(item)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item

@app.get("/item/{item_id}", response_model=ItemResponse)
def get_an_item(item_id: int, session: Session = Depends(get_session)):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item