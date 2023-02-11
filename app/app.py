from fastapi import FastAPI

app = FastAPI()

# let's do a minimal app
@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {"Ping": "Pong"}

# Read todo
@app.get('/todo', tags=['todos'])
async def get_todo() -> dict:
    return {"data":  todos}

@app.post("/todo", tags=["todos"])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return {
        "data": todos
    }

@app.put("/todo/{id}", tags=['todos'])
async def update_todo(id:int, body:dict) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todo["Activity"] = body["Activity"]

    return {
        "data": todos
    }

@app.delete("/todo/{id}", tags=['todos'])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo['id']) == id:
            todos.remove(todo)

    return {
        "data": todos
    }

todos = [
    {
        "id": "1",
        "Activity": "sex"

    },

    {
        "id": "2",
        "Activity": "Write a C++ app"

    }

]