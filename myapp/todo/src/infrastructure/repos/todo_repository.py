from typing import List

from myapp.todo.src.domain.repository import TodoRepository
from myapp.todo.src.domain.todo import Todo
from myapp.todo.src.infrastructure.datamodels.todo import Todo as TodoData, TodoProject


class FakeTodoRepository(TodoRepository):
    def find(self, id: str) -> List[Todo]:
        todos  = [
            TodoData(
                id="uasdfas",
                name="some name",
                description="some desc",
                todo_project=TodoProject(
                    id="asdfasdfas",
                    name="some_project name",
                )
            ),
            TodoData(
                id="uasdfas2",
                name="some name",
                description="some desc",
                todo_project=TodoProject(
                    id="asdfasdfas",
                    name="some_project name",
                )
            ),
            TodoData(
                id="uasdfas3",
                name="some name",
                description="some desc",
                todo_project=TodoProject(
                    id="asdfasdfas",
                    name="some_project name",
                )
            )
        ]

        result = []
        for todo in todos:
            result.append(
                Todo(
                    name=todo.name,
                    description=todo.description,
                    project=todo.todo_project.name
                )
            )

        return result



    def save(self, todo: Todo) -> None:
        return
