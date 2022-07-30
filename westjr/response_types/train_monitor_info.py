# [/api/v3/trainmonitorinfo.json]
from __future__ import annotations
from typing import List, Type

from typing_extensions import TypedDict


class Car(TypedDict):
    carNo: int
    status: int
    congestion: int
    temp: int
    facilities: list[int]
    types: list[int]


class Cars(TypedDict):
    cars: list[Car]


class TrainMonitorInfo(TypedDict):
    update: str
    trains: dict[str, List[Cars]]