from pydantic import BaseModel
from typing import List, Optional

#class AuthenticationIn(BaseModel):
#    name: str

#class AuthenticationOut(AuthenticationIn):
#    id: int


#class AuthenticationUpdate(AuthenticationIn):
#    name: Optional[str] = None


#modele user

class UserIn(BaseModel):
    name: str
    mail: str
    password: str
    token: str

class UserInTokenExp(UserIn):
    token_exp: int

class UserOut(UserInTokenExp):
    id: int

class UserUpdate(UserIn):
    name: Optional[str] = None
    mail: Optional[str] = None
    password: Optional[str] = None
    token: Optional[str] = None