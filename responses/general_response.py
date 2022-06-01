import json
from pydantic import BaseModel
from pydantic.class_validators import Optional
from requests import Response


class GeneralResponse(BaseModel):
    code: Optional[int]
    type: Optional[str]
    message: Optional[str]
    status_code: int

    @classmethod
    def get_response(cls, response: Response):
        if not response.text:
            return cls(status_code=response.status_code)
        return cls(status_code=response.status_code, **json.loads(response.text))
