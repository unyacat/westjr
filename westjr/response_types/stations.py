# [/api/v3/{LINE}_st.json]

from __future__ import annotations

from typing_extensions import TypedDict


class TransferItem(TypedDict):
    name: str
    type: int
    code: str
    link: str | None
    linkCode: str | None


class Info(TypedDict):
    name: str
    code: str
    stopTrains: list[int] | None
    typeNotice: str | None
    transfer: list[TransferItem] | None
    line: str | None
    pairDisplay: str | None
    lines: str | None


class SideItem(TypedDict):
    type: int
    side: int | None
    linkLine: str | None
    linkStationCode: str | None
    line: str
    linkDirection: int | None


class Design(TypedDict):
    mark: str | None
    upside: list[SideItem] | None
    downside: list[SideItem] | None


class StationsItem(TypedDict):
    info: Info
    design: Design


class Stations(TypedDict):
    stations: list[StationsItem]
