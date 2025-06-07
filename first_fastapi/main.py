from fastapi import FastAPI,Depends
import uvicorn
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

def get_message():
       return "Hello from dependency!"

# Inject the dependency into the route
@app.get("/items/")
async def read_items(message: str = Depends(get_message)):
    return {"message": message}
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

if __name__ == '__main__':
    uvicorn.run("main:app",reload=True)