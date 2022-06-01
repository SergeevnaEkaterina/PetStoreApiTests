import uuid
from models.pet import Pet
from models.category_pet import Category
from models.status_pet import Status
from models.tag_pet import Tag
import random


def generate_test_pet():
    pet = Pet(
        id=uuid.uuid4().node,
        name=uuid.uuid4().hex,
        category=Category(id=uuid.uuid4().node, name=uuid.uuid4().hex),
        status=random.choice(list(Status)),
        photoUrls=[],
        tags=[Tag(id=uuid.uuid4().node, name=uuid.uuid4().hex) for _ in range(random.randint(0, 5))]
    )

    print(pet)
    return pet
