# [/api/v3/area_{AREA}_master.json]
from typing import Dict, List, Optional, Union

from pydantic import BaseModel, Field


class Dest(BaseModel):
    upper: str
    lower: str


class Line(BaseModel):
    name: str
    range: str
    relatelines: Optional[List[str]]
    st: str
    pos: str
    index: int
    dest: Dest


class TrafficInfo(BaseModel):
    url: str


class DelayTextItemFrom(BaseModel):
    from_: int = Field(..., alias="from")
    display: int


class DelayTextItemTo(BaseModel):
    to: int
    display: int


class NoUpdateAlert(BaseModel):
    currentTime: str
    thresholdMinutes: int


class TrainmonitorinfoLine(BaseModel):
    info: str
    currentTime: str
    thresholdSeconds: int


TrainmonitorinfoLines = Dict[str, TrainmonitorinfoLine]


class AreaMaster(BaseModel):
    lines: Dict[str, Line]
    trafficInfo: TrafficInfo
    delayText: List[Union[DelayTextItemFrom, DelayTextItemTo]]
    noUpdateAlert: NoUpdateAlert
    trainmonitorinfoLines: TrainmonitorinfoLines
