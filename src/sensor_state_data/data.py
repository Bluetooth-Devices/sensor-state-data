from __future__ import annotations

import dataclasses
from abc import abstractmethod
from datetime import date, datetime
from decimal import Decimal
from typing import Any, Final, TypedDict

from .description import BaseSensorDescription, SensorDescription
from .device import DeviceKey
from .device_class import DeviceClass
from .value import SensorValue


class SensorDeviceInfo(TypedDict, total=False):

    name: str
    model: str
    manufacturer: str
    sw_version: str
    hw_version: str


ATTR_NAME: Final = "name"
ATTR_MODEL: Final = "model"
ATTR_MANUFACTURER: Final = "manufacturer"
ATTR_SW_VERSION: Final = "sw_version"
ATTR_HW_VERSION: Final = "hw_version"


@dataclasses.dataclass(frozen=True)
class SensorUpdate:

    title: str | None
    devices: dict[str | None, SensorDeviceInfo]
    entity_descriptions: dict[DeviceKey, SensorDescription]
    entity_values: dict[DeviceKey, SensorValue]


class SensorData:
    """Generate a sensor update."""

    def __init__(self) -> None:
        """Init sensor data."""
        self._title: str | None = None
        self._software_version: str | None = None
        self._device_id_info: dict[str | None, SensorDeviceInfo] = {}
        self._device_id_to_name: dict[str | None, str] = {}
        self._device_id_to_type: dict[str | None, str] = {}
        self._descriptions: dict[DeviceKey, SensorDescription] = {}
        self._descriptions_updates: dict[DeviceKey, SensorDescription] = {}
        self._values: dict[DeviceKey, SensorValue] = {}
        self._values_updates: dict[DeviceKey, SensorValue] = {}

    @property
    def descriptions(
        self,
    ) -> dict[DeviceKey, SensorDescription]:
        """Return the data."""
        return self._descriptions

    @property
    def primary_device_id(self) -> str | None:
        """Return the primary device id."""
        if self._device_id_to_type:
            return list(self._device_id_to_type)[0]
        return None

    @property
    def title(self) -> str | None:
        """Return the title."""
        return self._title

    def set_title(self, title: str) -> None:
        """Set the title."""
        self._title = title

    def set_device_manufacturer(
        self, manufacturer: str, device_id: str | None = None
    ) -> None:
        """Set the device manufacturer."""
        self._device_id_info.setdefault(device_id, {})[ATTR_MANUFACTURER] = manufacturer

    def set_device_hw_version(
        self, hw_version: str, device_id: str | None = None
    ) -> None:
        """Set the device hardware version."""
        self._device_id_info.setdefault(device_id, {})[ATTR_HW_VERSION] = hw_version

    def set_device_sw_version(
        self, sw_version: str, device_id: str | None = None
    ) -> None:
        """Set the device software version."""
        self._device_id_info.setdefault(device_id, {})[ATTR_SW_VERSION] = sw_version

    def set_device_name(self, name: str, device_id: str | None = None) -> None:
        """Set the device name."""
        self._device_id_to_name[device_id] = name
        self._device_id_info.setdefault(device_id, {})[ATTR_NAME] = name

    def set_device_type(self, device_type: str, device_id: str | None = None) -> None:
        """Set the device type."""
        self._device_id_to_type[device_id] = device_type
        self._device_id_info.setdefault(device_id, {})[ATTR_MODEL] = device_type

    @abstractmethod
    def _start_update(self, data: Any) -> None:
        """Update the data."""

    def supported(self, data: Any) -> bool:
        """Return True if the device is supported."""
        self._start_update(data)
        return bool(self._device_id_to_type)

    def update(self, data: Any) -> SensorUpdate:
        """Update a device."""
        self._start_update(data)
        return self._finish_update()

    def _finish_update(self) -> SensorUpdate:
        self._descriptions.update(self._descriptions_updates)
        self._values.update(self._values_updates)
        return SensorUpdate(
            title=self._title,
            devices=self._device_id_info,
            entity_descriptions=self._descriptions_updates,
            entity_values=self._values_updates,
        )

    def update_predefined_sensor(
        self,
        base_description: BaseSensorDescription,
        native_value: None | str | int | float | date | datetime | Decimal,
        key: str | None = None,
        name: str | None = None,
        device_id: str | None = None,
    ) -> None:
        """Update a sensor by type."""
        assert base_description.device_class is not None  # nosec
        self.update_sensor(
            key=key or base_description.device_class.value,
            name=name,
            native_unit_of_measurement=base_description.native_unit_of_measurement,
            native_value=native_value,
            device_class=base_description.device_class,
            device_id=device_id,
        )

    def _get_key_name(self, key: str, device_id: str | None = None) -> str:
        """Set the device name."""
        return key.replace("_", " ").title()

    def get_device_name(self, device_id: str | None = None) -> str | None:
        """Get the device name."""
        return self._device_id_to_name.get(device_id) or self._device_id_to_type.get(
            device_id
        )

    def update_sensor(
        self,
        key: str,
        native_unit_of_measurement: str | None,
        native_value: None | str | int | float | date | datetime | Decimal,
        device_class: DeviceClass | None = None,
        name: str | None = None,
        device_id: str | None = None,
    ) -> None:
        """Update a sensor."""
        device_key = DeviceKey(key, device_id)
        self._values_updates[device_key] = SensorValue(
            device_key=device_key,
            native_value=native_value,
        )
        self._descriptions_updates[device_key] = SensorDescription(
            device_key=device_key,
            name=name or self._get_key_name(key, device_id),
            native_unit_of_measurement=native_unit_of_measurement,
            device_class=device_class,
        )
