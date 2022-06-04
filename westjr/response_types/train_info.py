# [/api/v3/area_{AREA}_trafficinfo.json]
from __future__ import annotations

from typing_extensions import TypedDict

Section = TypedDict(
    "Section",
    {
        "from": str,
        "to": str,
    },
)


class Info_LineItem(TypedDict):
    count: int
    section: Section
    status: str
    mark: int
    cause: str
    transfer: bool
    url: str


class Info_ExpressItem(TypedDict):
    count: int
    unique: int
    name: str
    status: str
    mark: int
    cause: str
    url: str


class TrainInfo(TypedDict):
    lines: dict[str, Info_LineItem]
    express: dict[str, Info_ExpressItem]
