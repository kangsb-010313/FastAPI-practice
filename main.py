
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}

@app.get("/hello/{name}")
def read_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/hello")
def create_hello(name: str):
    return {"message": f"Hello {name}"}

@app.put("/hello/{name}")
def update_hello(name: str):
    return {"message": f"Hello {name}"}

@app.delete("/hello/{name}")
def delete_hello(name: str):
    return {"message": f"Hello {name}"}