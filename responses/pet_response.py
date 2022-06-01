from requests import Response
import json
from models.pet import Pet


class PetResponse:
    def __init__(self, status_code, **kwargs):
        self.pet = Pet(**kwargs)
        self.status_code = status_code

    @classmethod
    def build_from(cls, response: Response):
        return cls(status_code=response.status_code, **json.loads(response.text))
