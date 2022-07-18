from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal

from .device import DeviceKey


@dataclass(frozen=True)
class SensorValue:
    """A class that describes sensor values."""

    device_key: DeviceKey
    native_value: None | str | int | float | date | datetime | Decimal
