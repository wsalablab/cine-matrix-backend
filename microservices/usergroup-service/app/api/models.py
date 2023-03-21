from pydantic import BaseModel
from typing import List, Optional

class UsergroupIn(BaseModel):
    name: str

class UsergroupOut(UsergroupIn):
    id: int

class UsergroupUpdate(UsergroupIn):
    name: Optional[str] = None