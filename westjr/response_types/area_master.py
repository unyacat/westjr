# [/api/v3/area_{AREA}_master.json]
from __future__ import annotations

from typing import Dict

from typing_extensions import TypedDict


class Dest(TypedDict):
    upper: str
    lower: str


class _Line(TypedDict):
    name: str
    range: str
    st: str
    pos: str
    index: int
    dest: Dest


class Line(_Line, total=False):
    relatelines: list[str]


class TrafficInfo(TypedDict):
    url: str


DelayTextItemFrom = TypedDict(
    "DelayTextItemFrom",
    {
        "from": int,
        "display": int,
    },
)


class DelayTextItemTo(TypedDict):
    to: int
    display: int


class NoUpdateAlert(TypedDict):
    currentTime: str
    thresholdMinutes: int


class TrainmonitorinfoLine(TypedDict):
    info: str
    currentTime: str
    thresholdSeconds: int


TrainmonitorinfoLines = Dict[str, TrainmonitorinfoLine]

Lines = Dict[str, Line]


class AreaMaster(TypedDict):
    lines: Lines
    trafficInfo: TrafficInfo
    delayText: list[DelayTextItemFrom | DelayTextItemTo]
    noUpdateAlert: NoUpdateAlert
    trainmonitorinfoLines: TrainmonitorinfoLines
