from pydantic import BaseModel


class TodoRequest(BaseModel):
    name: str
    description: str | None = None
    project: str | None = None
