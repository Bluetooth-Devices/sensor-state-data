from __future__ import annotations

from dataclasses import dataclass

from .device_class import DeviceClass


@dataclass
class SensorDescription:
    """A class that describes sensors."""

    device_class: DeviceClass | None = None
    native_unit_of_measurement: str | None = None
