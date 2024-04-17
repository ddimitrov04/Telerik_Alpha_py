from fastapi import Response


class NoContent(Response):
    def __init__(self):
        super().__init__(status_code=204)


class InternalServerError(Response):
    def __init__(self):
        super().__init__(status_code=500)

class NotFound(Response):
    def __init__(self, content=''):
        super().__init__(status_code=404, content=content)