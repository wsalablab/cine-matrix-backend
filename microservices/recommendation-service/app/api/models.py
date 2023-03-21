from pydantic import BaseModel
from typing import List, Optional

class RecommendationIn(BaseModel):
    name: str

class RecommendationOut(RecommendationIn):
    id: int

class RecommendationUpdate(RecommendationIn):
    name: Optional[str] = None