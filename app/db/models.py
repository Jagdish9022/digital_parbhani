from pydantic import BaseModel
from typing import Optional

class Service(BaseModel):
    name: str
    type: str
    location: str
    address: str
    mobile_no: str
    timings: str
    cost: str
    available: bool
    latitude: float
    longitude: float
    contact: str

class UserQuery(BaseModel):
    query: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None