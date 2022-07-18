from __future__ import annotations

from dataclasses import dataclass

from .device import DeviceKey
from .device_class import DeviceClass


@dataclass(frozen=True)
class BaseSensorDescription:

    device_class: DeviceClass | None = None
    native_unit_of_measurement: str | None = None


@dataclass(frozen=True)
class SensorDescriptionIds:

    device_key: DeviceKey
    name: str | None = None


@dataclass(frozen=True)
class SensorDescription(BaseSensorDescription, SensorDescriptionIds):
    """A class that describes sensors."""
