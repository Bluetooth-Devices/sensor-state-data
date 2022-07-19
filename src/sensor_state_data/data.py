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


ATTR_NAME: Final = "name"
ATTR_MODEL: Final = "model"


@dataclasses.dataclass(frozen=True)
class SensorUpdate:

    devices: dict[str | None, SensorDeviceInfo]
    entity_descriptions: dict[DeviceKey, SensorDescription]
    entity_values: dict[DeviceKey, SensorValue]


class SensorData:
    """Generate a sensor update."""

    def __init__(self) -> None:
        """Init a bluetooth device."""
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

    def set_device_name(self, name: str, device_id: str | None = None) -> None:
        """Set the device name."""
        self._device_id_to_name[device_id] = name
        self._device_id_info.setdefault(device_id, {})[ATTR_NAME] = name

    def set_device_type(self, device_type: str, device_id: str | None = None) -> None:
        """Set the device type."""
        self._device_id_to_type[device_id] = device_type
        self._device_id_info.setdefault(device_id, {})[ATTR_MODEL] = device_type

    @abstractmethod
    def update(self, data: Any) -> None:
        """Update the data."""

    def supported(self, data: Any) -> bool:
        """Return True if the device is supported."""
        self.generate_update(data)
        return bool(self._device_id_to_type)

    def generate_update(self, data: Any) -> SensorUpdate:
        """Update a bluetooth device."""
        self.update(data)
        self._descriptions.update(self._descriptions_updates)
        self._values.update(self._values_updates)
        return SensorUpdate(
            devices=self._device_id_info,
            entity_descriptions=self._descriptions_updates,
            entity_values=self._values_updates,
        )

    def update_predefined_sensor(
        self,
        base_description: BaseSensorDescription,
        native_value: None | str | int | float | date | datetime | Decimal,
        name: str | None = None,
        device_id: str | None = None,
    ) -> None:
        """Update a sensor by type."""
        assert base_description.device_class is not None  # nosec
        self.update_sensor(
            key=base_description.device_class.value,
            name=name,
            native_unit_of_measurement=base_description.native_unit_of_measurement,
            native_value=native_value,
            device_class=base_description.device_class,
            device_id=device_id,
        )

    def _get_key_name(self, key: str, device_id: str | None = None) -> str:
        """Set the device name."""
        if device_name := self.get_device_name(device_id):
            return f"{device_name} {key.title()}"
        return key.title()

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
