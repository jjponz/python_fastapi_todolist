from typing import List

from myapp.todo.src.domain.repository import TodoRepository
from myapp.todo.src.domain.todo import Todo


class TodoFinder:
    def __init__(self, todo_repository: TodoRepository):
        self._todo_repository = todo_repository

    def execute(self, id: str) -> List[Todo]:
        return self._todo_repository.find(id)
