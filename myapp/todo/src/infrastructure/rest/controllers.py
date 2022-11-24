from fastapi import APIRouter, HTTPException

from myapp.todo.src.application.todo_creator import TodoCreator
from myapp.todo.src.application.todo_finder import TodoFinder
from myapp.todo.src.domain.exceptions import TodoWithoutNameException
from myapp.todo.src.infrastructure.repos.todo_repository import FakeTodoRepository
from myapp.todo.src.infrastructure.serializers.TodoSerializer import TodoSerializer
from myapp.todo.src.infrastructure.serializers.todo_request_serializer import TodoRequest

router = APIRouter(prefix='/todos')


@router.get("/{id}")
async def find_todo(id: str):
    todos = TodoFinder(FakeTodoRepository()).execute(id)

    return TodoSerializer(todos).data


@router.post("/")
async def create_todo(todo: TodoRequest):
    try:
        TodoCreator(FakeTodoRepository()).execute(
            todo.name,
            todo.description,
            todo.project
        )
    except TodoWithoutNameException:
        raise HTTPException(status_code=400, detail="Item not found")

    return "created"







