import requests
from responses.general_response import GeneralResponse
from responses.user_response import UserResponse
from models.user import User


class UserClient:
    base_url: str

    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2"

    def get_user_endpoints(self):
        return UserActions(self.base_url)


class UserActions:
    url: str

    def __init__(self, base_url):
        self.url = base_url + "/user"

    def create(self, user: User) -> GeneralResponse:
        headers = {'accept': 'application/json', 'Content-type': 'application/json'}
        response = requests.post(self.url, data=user.json(), headers=headers)
        print(user.json())
        return GeneralResponse.get_response(response)

    def find(self, user: User, get_user=None) -> UserResponse:
        headers = {'accept': 'application/json'}
        response = requests.get(f"{self.url}/{user.username}", headers=headers)
        return UserResponse.build_from(response, get_user)

    def find_invalid(self, user: User) -> GeneralResponse:
        headers = {'accept': 'application/json'}
        response = requests.get(f"{self.url}/{user.username}", headers=headers)
        return GeneralResponse.get_response(response)

    def update(self, existing_user: User, generated_user: User) -> GeneralResponse:
        headers = {'accept': 'application/json', 'Content-type': 'application/json'}
        response = requests.put(f"{self.url}/{existing_user.username}", data=generated_user.json(), headers=headers)
        return GeneralResponse.get_response(response)

    def delete(self, user: User) -> GeneralResponse:
        headers = {'accept': 'application/json'}
        response = requests.delete(f"{self.url}/{user.username}", headers=headers)
        return GeneralResponse.get_response(response)

    def login(self, user: User) -> GeneralResponse:
        headers = {'accept': 'application/json'}
        response = requests.get(f"{self.url}/login?username={user.username}&password={user.password}",
                                headers=headers)
        return GeneralResponse.get_response(response)
