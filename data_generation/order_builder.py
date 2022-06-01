import uuid
from models.order import Order
from models.status_order import Status
import random
from datetime import datetime


def generate_test_order():
    order = Order(
        id=uuid.uuid4().node,
        petId=uuid.uuid4().node,
        quantity=random.randint(0, 5),
        shipDate=datetime.now().strftime('%Y-%m-%d'+'T'+'%H:%M:%S.%f')[:-3]+'+0000',
        status=random.choice(list(Status)),
        complete=random.getrandbits(1)
        )

    print(order)
    return order
