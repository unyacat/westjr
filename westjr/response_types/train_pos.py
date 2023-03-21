# [/api/v3/{LINE}.json]
from typing import List

from pydantic import BaseModel


class Dest(BaseModel):
    text: str
    code: str
    line: str


class TrainsItem(BaseModel):
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


class TrainPos(BaseModel):
    update: str
    trains: List[TrainsItem]
