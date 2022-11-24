from typing import List

from myapp.todo.src.domain.todo import Todo


class TodoRepository:
    def find(self, id: str) -> List[Todo]:
        raise NotImplementedError()

    def save(self, todo: Todo) -> None:
        raise NotImplementedError()
