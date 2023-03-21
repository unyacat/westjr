# [/api/v3/area_{AREA}_trafficinfo.json]
from typing import Dict

from pydantic import BaseModel, Field


class Section(BaseModel):
    from_: str = Field(..., alias="from")
    to: str


class Info_LineItem(BaseModel):
    count: int
    section: Section
    status: str
    mark: int
    cause: str
    transfer: bool
    url: str


class Info_ExpressItem(BaseModel):
    count: int
    unique: int
    name: str
    status: str
    mark: int
    cause: str
    url: str


class TrainInfo(BaseModel):
    lines: Dict[str, Info_LineItem]
    express: Dict[str, Info_ExpressItem]
