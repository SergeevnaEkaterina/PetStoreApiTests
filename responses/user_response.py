from requests import Response
import json
from models.user import User


class UserResponse:
    def __init__(self, status_code, **kwargs):
        self.user = User(**kwargs)
        self.status_code = status_code

    @classmethod
    def build_from(cls, response: Response, get_schema: bool = None):
        if get_schema:
            return json.loads(response.text)
        return cls(status_code=response.status_code, **json.loads(response.text))
