from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal

from .device import DeviceKey


@dataclass(frozen=True)
class BaseValue:
    device_key: DeviceKey
    name: str | None


@dataclass(frozen=True)
class SensorValue(BaseValue):
    """A class that describes sensor values."""

    native_value: str | int | float | date | datetime | Decimal | None


@dataclass(frozen=True)
class BinarySensorValue(BaseValue):
    """A class that describes sensor values."""

    native_value: bool | None


@dataclass(frozen=True)
class Event(BaseValue):
    """A class that describes device events."""

    event_type: str
    event_properties: dict[str, str | int | float | None] | None
