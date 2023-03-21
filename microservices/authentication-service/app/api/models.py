from pydantic import BaseModel
from typing import List, Optional

class AuthenticationIn(BaseModel):
    name: str

class AuthenticationOut(AuthenticationIn):
    id: int


class AuthenticationUpdate(AuthenticationIn):
    name: Optional[str] = None