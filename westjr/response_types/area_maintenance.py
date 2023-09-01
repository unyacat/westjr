# [/api/v3/area_{AREA}_maintenance.json]
from __future__ import annotations

from pydantic import BaseModel


class Notification(BaseModel):
    groupId: int
    text: str
    duration: str


class Maintenance(BaseModel):
    title: str
    text: str
    duration: str
    linkTitle: str
    linkUrl: str


class AreaMaintenance(BaseModel):
    status: int
    notification: Notification
    maintenance: Maintenance
