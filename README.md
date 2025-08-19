# Task Manager API
FastAPI + gauge 

REST API для управления задачами с поддержкой CRUD.
---

## 🚀 Быстрый старт с Docker

1. **Собрать Docker-образ:**

```bash
docker build -t taskmanager:latest .
```
2. **Запустить контейнер:**

```bash
docker run -p 8000:8000 taskmanager:latest
```
## Запуск тестов с локальной машины
**После запуска контейнера в корне проекта выполнить:**

```bash
gauge run specs
```
