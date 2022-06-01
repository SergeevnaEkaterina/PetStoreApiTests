import uuid
from models.user import User
import random


def generate_test_user():
    user = User(
        id=uuid.uuid4().node,
        username=uuid.uuid4().hex,
        firstName=uuid.uuid4().hex,
        lastName=uuid.uuid4().hex,
        email=uuid.uuid4().hex,
        password=uuid.uuid4().hex,
        phone=uuid.uuid4().hex,
        userStatus=random.randint(0, 100)
    )

    print(user)
    return user
