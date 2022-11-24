from dataclasses import asdict


class TodoSerializer:
    def __init__(self, todos):
        self._todos = todos

    @property
    def data(self):
        result = []
        for todo in self._todos:
            result.append(
                {key: str(value) for key, value in asdict(todo).items()}
            )
        return result
