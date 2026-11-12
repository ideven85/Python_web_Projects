from sqlmodel import create_engine, Session
DATABASE_URL = "postgresql+psycopg://deven:728000@localhost:5432/shopping_cart"
engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session