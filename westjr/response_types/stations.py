# [/api/v3/{LINE}_st.json]
from __future__ import annotations

from typing import List

from pydantic import BaseModel


class TransferItem(BaseModel):
    name: str
    type: int
    code: str
    link: str | None
    linkCode: str | None
    note: str | None = None
    substitute: bool | None = False


class PairDisplayItem(BaseModel):
    code: str
    position: int


class Info(BaseModel):
    name: str
    code: str
    stopTrains: List[int] | None
    typeNotice: str | None
    transfer: List[TransferItem] | None
    line: str | None = None
    pairDisplay: PairDisplayItem | None = None
    lines: str | None = None
    colorCode: str | None = None
    transferIcons: List[int] | None = None
    notDisplayType: int | None = None
    notDisplayNotices: List[str] | None = None
    end: bool | None = False


class SideItem(BaseModel):
    type: int
    side: int | None
    linkLine: str | None
    linkStationCode: str | None
    line: str | None = None
    linkDirection: int | None = None
    colorCode: str | None = None


class Design(BaseModel):
    mark: str | None
    upside: List[SideItem] | None
    downside: List[SideItem] | None


class StationsItem(BaseModel):
    info: Info
    design: Design


class Stations(BaseModel):
    stations: List[StationsItem]
