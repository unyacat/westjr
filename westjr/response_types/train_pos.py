# [/api/v3/{LINE}.json]
from __future__ import annotations

from typing import List, Union

from pydantic import BaseModel


class Dest(BaseModel):
    text: str
    code: str
    line: str


class TrainsItem(BaseModel):
    no: str
    pos: str
    direction: int
    nickname: Union[str, List[str], None]
    type: str
    displayType: str
    dest: Union[Dest, str]
    via: str | None = None
    delayMinutes: int
    aSeatInfo: str | None = None
    typeChange: str | None = None
    numberOfCars: int | None = None


class TrainPos(BaseModel):
    update: str
    trains: List[TrainsItem]
