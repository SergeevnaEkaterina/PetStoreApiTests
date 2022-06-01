from requests import Response
import json
from models.order import Order


class OrderResponse:
    def __init__(self, status_code, **kwargs):
        self.order = Order(**kwargs)
        self.status_code = status_code

    @classmethod
    def get_response(cls, response: Response):
        return cls(status_code=response.status_code, **json.loads(response.text))
