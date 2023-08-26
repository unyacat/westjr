# [/api/v3/area_{AREA}_trafficinfo.json]
from __future__ import annotations

from typing import Dict, Optional

from pydantic import BaseModel, Field


class Section(BaseModel):
    from_: Optional[str] = Field(..., alias="from")
    to: Optional[str] = None


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
