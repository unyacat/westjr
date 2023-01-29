from __future__ import annotations

from typing import Any, TypeVar, cast

from pydantic import create_model_from_typeddict

_T = TypeVar("_T")


def parse_data_from_typeddict(typeddict_cls: type[_T], data: Any) -> _T:
    Model = create_model_from_typeddict(typeddict_cls)
    m = Model(**data).dict()
    return cast(_T, m)


__all__ = ("parse_data_from_typeddict",)
