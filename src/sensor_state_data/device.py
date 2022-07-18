from __future__ import annotations

import dataclasses


@dataclasses.dataclass(frozen=True)
class DeviceKey:
    """Key for a device.

    Example:
    device_id: outdoor_sensor_1
    key: temperature
    """

    key: str
    device_id: str | None = None
