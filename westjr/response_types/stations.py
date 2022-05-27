# [/api/v3/{LINE}_st.json]

from __future__ import annotations

from typing import TypedDict


class TransferItem(TypedDict):
    name: str
    type: int
    code: str
    link: str
    linkCode: str


class Info(TypedDict):
    name: str
    code: str
    stopTrains: list[int] | str
    typeNotice: str
    transfer: list[TransferItem] | str
    line: str
    pairDisplay: str
    lines: str


class UpsideItem(TypedDict):
    type: int
    side: int | str
    linkLine: str
    linkStationCode: str
    line: str
    linkDirection: str


class DownsideItem(TypedDict):
    type: int
    side: int | str
    linkLine: str
    linkStationCode: str
    line: str
    linkDirection: str


class Design(TypedDict):
    mark: str
    upside: list[UpsideItem] | str
    downside: list[DownsideItem] | str


class StationsItem(TypedDict):
    info: Info
    design: Design


class Stations(TypedDict):
    stations: list[StationsItem]
