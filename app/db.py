from typing import Dict
from uuid import UUID
from .models import Task

db: Dict[UUID, Task] = {}
