# [/api/v3/{LINE}.json]
from __future__ import annotations

from typing import List, Optional, Union

from pydantic import BaseModel


class Dest(BaseModel):
    text: str
    code: str
    line: str


class TrainsItem(BaseModel):
    no: str
    pos: str
    direction: int
    nickname: Union[Optional[str], Optional[List[str]]]
    type: str
    displayType: str
    dest: Union[Dest, str]
    via: Optional[str] = None
    delayMinutes: int
    aSeatInfo: Optional[str] = None
    typeChange: Optional[str] = None
    numberOfCars: Optional[int] = None


class TrainPos(BaseModel):
    update: str
    trains: List[TrainsItem]
