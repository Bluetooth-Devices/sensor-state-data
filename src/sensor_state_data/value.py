from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal


@dataclass
class SensorValue:
    """A class that describes sensor values."""

    native_value: None | str | int | float | date | datetime | Decimal
