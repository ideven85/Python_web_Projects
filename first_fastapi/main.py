# from fastapi import FastAPI,Depends
import uvicorn
from pathlib import Path
import sys
import uvicorn

# Point Python to the "src/first_fastapi" folder
target_dir = Path(__file__).resolve().parent / "src" / "first_fastapi"
sys.path.insert(0, str(target_dir))

#from pydantic.v1 import validator
#
# app = FastAPI()
# PASSWORD_REGEX = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])\S{8,64}$'
#
# class UserCreate(BaseModel):
#     id: str
#     name: str = Field(...,min_length=3,max_length=30)
#     username:str = Field(...,min_length=3,max_length=30)
#     password: str = Field(...,min_length=8, max_length=20)
#     confirm_password: str
#     #
#     @field_validator("password")
#     @classmethod
#     def validate_password(cls,value:str)->str:
#         if not re.search(r"[A-Z]",value):
#             raise ValueError("Password must contain a upper character")
#         if not re.search(r"[a-z]", value):
#             raise ValueError("Password must contain a lower character")
#         if not re.search(r"\d", value):
#             raise ValueError("Password must contain a digit")
#         if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
#             raise ValueError("Password must contain a special character")
#         if " " in value:
#             raise ValueError("Password must not contain spaces")
#         return value
#
#
#     @model_validator(mode="after")
#     def varify_passwords(self):
#         if not self.password==self.confirm_password:
#             raise ValueError("Passwords do not match")
#         return self
#
# @app.post("/users/register")
# def register_user(user: UserCreate)->dict:
#     return {"message":f"{user.name} created successfully"}
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
# def get_message():
#        return "Hello from dependency!"
#
# # Inject the dependency into the route
# @app.get("/items/")
# async def read_items(message: str = Depends(get_message)):
#     return {"message": message}
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}

if __name__ == '__main__':
    uvicorn.run("app:app",host='localhost',reload=True)