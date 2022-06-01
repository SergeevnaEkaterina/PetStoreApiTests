import pytest_check as c
from checkers import checkers as check
from clients.pet_client import PetClient
from models.pet import Pet


class TestPet:

    def test_create_pet(self, generated_pet):
        create_pet_response = PetClient().get_pet_endpoints().create(generated_pet)
        check.validate_pet(create_pet_response, 200, generated_pet)

    def test_update_pet_with_store_data(self, generated_pet, existing_pet):
        generated_pet.id = existing_pet.id
        create_pet_response = PetClient().get_pet_endpoints().update(generated_pet)
        check.check_default_response(create_pet_response, 200, 'unknown', str(generated_pet.id))

    def test_update_with_store_data_not_existing_pet(self, generated_pet, existing_pet):
        generated_pet.id = existing_pet.id + 1
        create_pet_response = PetClient().get_pet_endpoints().update(generated_pet)
        check.check_default_response(create_pet_response, 404, 'unknown', 'not found')

    def test_delete_pet(self, generated_pet):
        PetClient().get_pet_endpoints().create(generated_pet)
        delete_pet_response = PetClient().get_pet_endpoints().delete(generated_pet.id)
        check.check_default_response(delete_pet_response, 200, 'unknown', str(generated_pet.id))

    def test_delete_not_existing_pet(self, generated_pet):
        PetClient().get_pet_endpoints().create(generated_pet)
        generated_pet.id += 1
        delete_pet_response = PetClient().get_pet_endpoints().delete(generated_pet)
        c.equal(delete_pet_response.status_code, 404)

    def test_find_pet_by_status(self, existing_pet):
        create_pet_response = PetClient().get_pet_endpoints().find(existing_pet)
        c.equal(create_pet_response.status_code, 200)
        c.equal(all([pet.__class__ == Pet for pet in create_pet_response.pets]), True)
