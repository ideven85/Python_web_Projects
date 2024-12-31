from typing import Optional

import fastapi
import uvicorn
from fastapi import FastAPI
from fastapi_crud import FastapiCRUD
import pandas as pd

# import py_eureka_client.eureka_client as eureka_client

app = FastAPI()


@app.get("/")
async def index():
    return {"Hello": "World"}


@app.get("/employee/{name}/branch/{branch_id}")
async def get_employee(
    name: str, brname: str, branch_id: int, age: Optional[int] = None
):
    employee = {"name": name, "Branch": brname, "Branch ID": branch_id, "age": age}
    return employee


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
