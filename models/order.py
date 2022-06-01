from pydantic import BaseModel
from models import status_order


class Order(BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: str
    status: status_order.Status
    complete: bool
