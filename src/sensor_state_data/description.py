from __future__ import annotations

from dataclasses import dataclass

from .base import BaseDeviceClass
from .binary_sensor.device_class import BinarySensorDeviceClass
from .device import DeviceKey
from .sensor.device_class import SensorDeviceClass
from .units import Units


@dataclass(frozen=True, slots=True)
class BaseDescription:
    """A base class for all descriptions."""

    device_class: BaseDeviceClass | None = None


@dataclass(frozen=True, slots=True)
class BaseBinarySensorDescription(BaseDescription):

    device_class: BinarySensorDeviceClass | None = None


@dataclass(frozen=True, slots=True)
class BaseSensorDescription(BaseDescription):

    device_class: SensorDeviceClass | None = None
    native_unit_of_measurement: Units | None = None


@dataclass(frozen=True, slots=True)
class SensorDescriptionIds:

    device_key: DeviceKey


@dataclass(frozen=True, slots=True)
class KeyedBaseDescription(BaseDescription, SensorDescriptionIds):
    """A class for sensors that use a key."""


@dataclass(frozen=True, slots=True)
class SensorDescription(BaseSensorDescription, KeyedBaseDescription):
    """A class that describes sensors."""


@dataclass(frozen=True, slots=True)
class BinarySensorDescription(BaseBinarySensorDescription, KeyedBaseDescription):
    """A class that describes binary sensors."""
