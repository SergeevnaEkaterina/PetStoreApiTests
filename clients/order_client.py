import requests
from responses.general_response import GeneralResponse
from responses.order_response import OrderResponse
from models.order import Order


class OrderClient:
    base_url: str

    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2"

    def get_order_endpoints(self):
        return OrderActions(self.base_url)


class OrderActions:
    url: str

    def __init__(self, base_url):
        self.url = base_url + "/store"

    def create(self, order: Order) -> OrderResponse:
        headers = {'accept': 'application/json', 'Content-type': 'application/json'}
        response = requests.post(f"{self.url}/order", data=order.json(), headers=headers)
        return OrderResponse.get_response(response)

    def find(self, order: Order) -> OrderResponse:
        headers = {'accept': 'application/json'}
        response = requests.get(f"{self.url}/order/{order.id}", headers=headers)
        return OrderResponse.get_response(response)

    def find_invalid(self, order: Order) -> GeneralResponse:
        headers = {'accept': 'application/json'}
        response = requests.get(f"{self.url}/order/{order.id}", headers=headers)
        return GeneralResponse.get_response(response)

    def delete(self, order: Order) -> GeneralResponse:
        headers = {'accept': 'application/json'}
        response = requests.delete(f"{self.url}/order/{order.id}", headers=headers)
        return GeneralResponse.get_response(response)
