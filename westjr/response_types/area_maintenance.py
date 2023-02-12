# [/api/v3/area_{AREA}_maintenance.json]
from __future__ import annotations

from typing_extensions import TypedDict


class Notification(TypedDict):
    groupId: int
    text: str
    duration: str


class Maintenance(TypedDict):
    title: str
    text: str
    duration: str
    linkTitle: str
    linkUrl: str


class AreaMaintenance(TypedDict):
    status: int
    notification: Notification
    maintenance: Maintenance
