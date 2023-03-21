from pydantic import BaseModel
from typing import List, Optional

class MovieIn(BaseModel):
    name: str

class MovieOut(MovieIn):
    id: int

class MovieUpdate(MovieIn):
    name: Optional[str] = None