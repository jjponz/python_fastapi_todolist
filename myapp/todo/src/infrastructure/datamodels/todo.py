from dataclasses import dataclass


# se mapea con la tabla projects con únicamente los atributos necesarios,
# de está manera los imports siguen estando ordenados

@dataclass
class TodoProject:
    id: str
    name: str


@dataclass
class Todo:
    id: str
    name: str
    description: str
    todo_project: TodoProject
