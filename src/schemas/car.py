from pydantic import BaseModel
from typing import Optional


class CarFilterSchema(BaseModel):
    color: Optional[str] = None
    model: Optional[str] = None
    brand: Optional[str] = None
    year: Optional[int] = None
    fuel: Optional[str] = None
    cylinders: Optional[int] = None
    power: Optional[float] = None
    gearshift: Optional[str] = None
    weight: Optional[int] = None
    seats: Optional[int] = None
    abs: Optional[bool] = None

class CarSchema(BaseModel):
    color: str
    model: str
    brand: str
    year: int
    fuel: str
    cylinders: int
    power: float
    gearshift: str
    weight: int
    seats: int
    abs: bool