import requests
from responses.general_response import GeneralResponse
from responses.pet_response import PetResponse
from responses.pet_array_response import PetArrayResponse
from models.pet import Pet


class PetClient:
    base_url: str

    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2"

    def get_pet_endpoints(self):
        return PetActions(self.base_url)


class PetActions:
    url: str

    def __init__(self, base_url):
        self.url = base_url + "/pet"

    def create(self, user: Pet) -> PetResponse:
        headers = {'Content-type': 'application/json'}
        response = requests.post(self.url, data=user.json(), headers=headers)
        return PetResponse.build_from(response)

    def find(self, pet: Pet, get_pet: bool = None) -> PetArrayResponse:
        headers = {'accept': 'application/json'}
        response = requests.get(f"{self.url}/findByStatus?status={pet.status.value}", headers=headers)
        return PetArrayResponse.get_response(response, get_pet)

    def delete(self, username) -> GeneralResponse:
        headers = {'api_key': 'special_key'}
        response = requests.delete(f"{self.url}/{username}", headers=headers)
        return GeneralResponse.get_response(response)

    def update(self, pet: Pet) -> GeneralResponse:
        headers = {'accept': 'application/json', 'Content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(f"{self.url}/{pet.id}", data=f"name={pet.name}&status={pet.status}", headers=headers)
        return GeneralResponse.get_response(response)
