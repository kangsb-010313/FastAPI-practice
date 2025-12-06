
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

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



class Todo(BaseModel):
    id: int
    title: str

todos: List[Todo] = []

@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

@app.get("/todos")
def read_todos():
    return todos

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            todos[i] = todo
            return todo
    return {"error": "Todo not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            del todos[i]
            return {"message": "deleted"}
    return {"error": "Todo not found"}
