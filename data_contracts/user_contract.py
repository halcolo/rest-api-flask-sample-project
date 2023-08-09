from pydantic import BaseModel

class UserContract(BaseModel):
    id: int
    name: str
    email: str
    age: int