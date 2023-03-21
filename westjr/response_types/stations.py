# [/api/v3/{LINE}_st.json]
from typing import List, Optional

from pydantic import BaseModel


class TransferItem(BaseModel):
    name: str
    type: int
    code: str
    link: Optional[str]
    linkCode: Optional[str]


class Info(BaseModel):
    name: str
    code: str
    stopTrains: Optional[List[int]]
    typeNotice: Optional[str]
    transfer: Optional[List[TransferItem]]
    line: Optional[str]
    pairDisplay: Optional[str]
    lines: Optional[str]


class SideItem(BaseModel):
    type: int
    side: Optional[int]
    linkLine: Optional[str]
    linkStationCode: Optional[str]
    line: str
    linkDirection: Optional[int]


class Design(BaseModel):
    mark: Optional[str]
    upside: Optional[List[SideItem]]
    downside: Optional[List[SideItem]]


class StationsItem(BaseModel):
    info: Info
    design: Design


class Stations(BaseModel):
    stations: List[StationsItem]
