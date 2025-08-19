from enum import Enum
from pydantic import BaseModel, Field
from uuid import UUID, uuid4


class TaskStatus(str, Enum):
    created = "created"
    in_progress = "in_progress"
    completed = "completed"


class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    description: str | None = None
    status: TaskStatus = TaskStatus.created


class TaskCreate(BaseModel):
    title: str
    description: str | None = None


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: TaskStatus | None = None
