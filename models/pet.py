from models import status_pet, category_pet, tag_pet
from pydantic import BaseModel
from typing import List, Any


class Pet(BaseModel):
    id: int
    category: category_pet.Category | None
    name: str | None
    status: status_pet.Status | None
    photoUrls: List[Any] | None
    tags: List[tag_pet.Tag] | None


class PetList(BaseModel):
    pet_list: List[Pet]
