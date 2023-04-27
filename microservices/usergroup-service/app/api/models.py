from pydantic import BaseModel
from typing import List, Optional

class UsergroupIn(BaseModel):
    name: str

class UsergroupOut(UsergroupIn):
    id: int

class UsergroupUpdate(UsergroupIn):
    name: Optional[str] = None

class GroupIn(BaseModel):
    name: str

class GroupOut(GroupIn):
    id: int

class GroupUpdate(GroupIn):
    name: Optional[str] = None

class UserGroup(BaseModel):
    id_group: int
    id_user: int
