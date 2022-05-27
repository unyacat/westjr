# [/api/v3/{LINE}.json]
from __future__ import annotations

from typing import TypedDict


class Dest(TypedDict):
    text: str
    code: str
    line: str


class TrainsItem(TypedDict):
    no: str
    pos: str
    direction: int
    nickname: str
    type: str
    displayType: str
    dest: Dest
    via: str
    delayMinutes: int
    typeChange: str
    numberOfCars: int


class TrainPos(TypedDict):
    update: str
    trains: list[TrainsItem]
