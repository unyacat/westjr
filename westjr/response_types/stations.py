# [/api/v3/{LINE}_st.json]
from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class TransferItem(BaseModel):
    name: str
    type: int
    code: str
    link: Optional[str]
    linkCode: Optional[str]
    note: Optional[str] = None
    substitute: Optional[bool] = False

class PairDisplayItem(BaseModel):
    code: str
    position: int

class Info(BaseModel):
    name: str
    code: str
    stopTrains: Optional[List[int]]
    typeNotice: Optional[str]
    transfer: Optional[List[TransferItem]]
    line: Optional[str] = None
    pairDisplay: Optional[PairDisplayItem] = None
    lines: Optional[str] = None
    colorCode: Optional[str] = None
    transferIcons: Optional[List[int]] = None
    notDisplayType: Optional[int] = None
    notDisplayNotices: Optional[List[str]] = None
    end: Optional[bool] = False

class SideItem(BaseModel):
    type: int
    side: Optional[int]
    linkLine: Optional[str]
    linkStationCode: Optional[str]
    line: Optional[str] = None
    linkDirection: Optional[int] = None
    colorCode: Optional[str] = None


class Design(BaseModel):
    mark: Optional[str]
    upside: Optional[List[SideItem]]
    downside: Optional[List[SideItem]]


class StationsItem(BaseModel):
    info: Info
    design: Design


class Stations(BaseModel):
    stations: List[StationsItem]
