from fastapi import FastAPI, HTTPException
from .models import Task, TaskCreate, TaskUpdate
from .db import db
from uuid import UUID


app = FastAPI(title="Task Manager API")


@app.post("/tasks", response_model=Task)
def create_task(task_data: TaskCreate):
    task = Task(**task_data.model_dump())
    db[task.id] = task
    return task


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str):
    try:
        key = UUID(task_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID")
    
    task = db.get(key)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return list(db.values())


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, task_update: TaskUpdate):
    try:
        key = UUID(task_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID")
    
    task = db.get(key)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    update_data = task_update.model_dump(exclude_unset=True)
    updated_task = task.model_copy(update=update_data)
    db[key] = updated_task
    return updated_task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    try:
        key = UUID(task_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID")
    
    if key not in db:
        raise HTTPException(status_code=404, detail="Task not found")
    del db[key]
    return {"message": "Task deleted"}
   