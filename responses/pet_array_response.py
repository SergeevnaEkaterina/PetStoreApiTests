from requests import Response
import json
from models.pet import Pet


class PetArrayResponse:
    def __init__(self, status_code, pets=None):
        if pets is None:
            pets = []
        self.pets = [Pet(**pet) for pet in pets]
        self.status_code = status_code

    @classmethod
    def get_response(cls, response: Response, get_schema: bool = None):
        if get_schema: return json.loads(response.text)
        return cls(status_code=response.status_code, pets=json.loads(response.text))
