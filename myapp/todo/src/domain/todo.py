from dataclasses import dataclass


@dataclass
class Todo:
    name: str
    description: str = None
    project: str = None
