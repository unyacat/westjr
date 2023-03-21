# [/api/v3/trainmonitorinfo.json]
from typing import Dict, List

from pydantic import BaseModel


class Car(BaseModel):
    carNo: int
    status: int
    congestion: int
    temp: int
    facilities: List[int]
    types: List[int]


class Cars(BaseModel):
    cars: List[Car]


class TrainMonitorInfo(BaseModel):
    update: str
    trains: Dict[str, List[Cars]]
