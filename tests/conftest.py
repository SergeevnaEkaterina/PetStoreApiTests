import pytest

from clients.order_client import OrderClient
from clients.pet_client import PetClient
from clients.user_client import UserClient
from data_generation.order_builder import generate_test_order
from data_generation.pet_builder import generate_test_pet
from data_generation.user_builder import generate_test_user


@pytest.fixture(autouse=True)
def existing_pet():
    pet = generate_test_pet()
    PetClient().get_pet_endpoints().create(pet)
    yield pet


@pytest.fixture(autouse=True)
def generated_pet():
    yield generate_test_pet()


@pytest.fixture(autouse=True)
def existing_order():
    order = generate_test_order()
    OrderClient().get_order_endpoints().create(order)
    yield order


@pytest.fixture(autouse=True)
def generated_order():
    yield generate_test_order()


@pytest.fixture(scope="function")
def generated_user():
    yield generate_test_user()


@pytest.fixture(scope="function")
def existing_user():
    user = generate_test_user()
    UserClient().get_user_endpoints().create(user)
    yield user
