from myapp.todo.src.domain.repository import TodoRepository
from myapp.todo.src.domain.todo import Todo, TodoName


class TodoCreator:
    def __init__(self, todo_repository: TodoRepository):
        self._repo = todo_repository

    def execute(self, name, description, project):
        todo = Todo(TodoName.create(name), description, project)
        self._repo.save(todo)
