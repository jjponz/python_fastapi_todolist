from unittest.mock import patch

import pytest

from myapp.todo.src.application.todo_creator import TodoCreator
from myapp.todo.src.domain.exceptions import TodoWithoutNameException
from myapp.todo.src.domain.repository import TodoRepository


class TestTodoCreator:
    @pytest.fixture
    def todo_repo(self):
        with patch.object(TodoRepository, 'save') as mock:
            yield mock

    def test_create_course(self, todo_repo):
        TodoCreator(TodoRepository()).execute(
            'name',
            'description',
            'project'
        )

        todo_repo.assert_called()

    def test_create_course_raise_exception_when_no_name(self, todo_repo):
        with pytest.raises(TodoWithoutNameException):
            TodoCreator(todo_repo).execute(
                '',
                'description',
                'project'
            )

        todo_repo.assert_not_called()
