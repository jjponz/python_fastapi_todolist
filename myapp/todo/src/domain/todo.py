from dataclasses import dataclass

from myapp.todo.src.domain.exceptions import TodoWithoutNameException


@dataclass
class TodoName:
    name: str

    @staticmethod
    def create(name):
        if not name:
            raise TodoWithoutNameException()

        return TodoName(name)

@dataclass
class Todo:
    name: TodoName
    description: str = None
    project: str = None
