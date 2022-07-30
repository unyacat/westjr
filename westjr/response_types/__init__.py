from __future__ import annotations

from typing import Union

from . import area_master, stations, train_info, train_pos
from .area_master import AreaMaster
from .stations import Stations
from .train_info import TrainInfo
from .train_pos import TrainPos, TrainsItem
from .train_monitor_info import TrainMonitorInfo


ResponseDict = Union[AreaMaster, Stations, TrainInfo, TrainPos, TrainMonitorInfo]

__all__ = [
    "area_master",
    "stations",
    "train_info",
    "train_pos",
    "train_monitor_info",
    "AreaMaster",
    "Stations",
    "TrainInfo",
    "TrainPos",
    "ResponseDict",
    "TrainsItem",
    "TrainMonitorInfo"
]
