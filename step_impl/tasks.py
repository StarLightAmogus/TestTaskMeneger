import requests
from getgauge.python import step

BASE_URL = "http://localhost:8000"
task_id = None

@step("Создать задачу")
def create_task():
    global task_id
    resp = requests.post(f"{BASE_URL}/tasks", json={"title": "Test Task", "description": "Demo"})
    print(f"POST /tasks -> {resp.status_code}, {resp.text}")
    assert resp.status_code in (200, 201), f"Failed to create task: {resp.status_code}"
    task_id = resp.json()["id"]
    print(f"Создана задача с ID: {task_id}")

@step("Получить задачу по ID")
def get_task_by_id():
    assert task_id is not None, "task_id ещё не создан!"
    resp = requests.get(f"{BASE_URL}/tasks/{task_id}")
    print(f"GET /tasks/{task_id} -> {resp.status_code}, {resp.text}")
    assert resp.status_code == 200, f"Failed to get task: {resp.status_code}"
    data = resp.json()
    assert data["id"] == task_id, f"ID задачи не совпадает: {data['id']} != {task_id}"

@step("Обновить задачу")
def update_task():
    assert task_id is not None, "task_id ещё не создан!"
    resp = requests.put(f"{BASE_URL}/tasks/{task_id}", json={"status": "in_progress"})
    print(f"PUT /tasks/{task_id} -> {resp.status_code}, {resp.text}")
    assert resp.status_code == 200, f"Failed to update task: {resp.status_code}"
    data = resp.json()
    assert data["status"] == "in_progress", f"Статус не обновлён: {data['status']}"

@step("Удалить задачу")
def delete_task():
    assert task_id is not None, "task_id ещё не создан!"
    resp = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    print(f"DELETE /tasks/{task_id} -> {resp.status_code}, {resp.text}")
    assert resp.status_code == 200, f"Failed to delete task: {resp.status_code}"
