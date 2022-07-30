# [/api/v3/trainmonitorinfo.json]
from __future__ import annotations

from typing import List, Dict

from typing_extensions import TypedDict


class Car(TypedDict):
    carNo: int
    status: int
    congestion: int
    temp: int
    facilities: List[int]
    types: List[int]


class Cars(TypedDict):
    cars: List[Car]


class TrainMonitorInfo(TypedDict):
    update: str
    trains: Dict[str, List[Cars]]
