from __future__ import annotations

import dataclasses
from abc import abstractmethod
from datetime import date, datetime
from decimal import Decimal
from typing import Any

from .binary_sensor.device_class import BinarySensorDeviceClass
from .description import (
    BaseSensorDescription,
    BinarySensorDescription,
    SensorDescription,
)
from .device import DeviceKey
from .sensor.device_class import SensorDeviceClass
from .units import Units
from .value import BinarySensorValue, Event, SensorValue

_PRECISION_SENTINEL = -1


@dataclasses.dataclass(frozen=False)
class SensorDeviceInfo:
    name: str | None
    model: str | None
    manufacturer: str | None
    sw_version: str | None
    hw_version: str | None


@dataclasses.dataclass(frozen=True)
class SensorUpdate:
    title: str | None
    devices: dict[str | None, SensorDeviceInfo]
    entity_descriptions: dict[DeviceKey, SensorDescription] = dataclasses.field(
        default_factory=dict
    )
    entity_values: dict[DeviceKey, SensorValue] = dataclasses.field(
        default_factory=dict
    )
    binary_entity_descriptions: dict[DeviceKey, BinarySensorDescription] = (
        dataclasses.field(default_factory=dict)
    )
    binary_entity_values: dict[DeviceKey, BinarySensorValue] = dataclasses.field(
        default_factory=dict
    )
    events: dict[DeviceKey, Event] = dataclasses.field(default_factory=dict)


class SensorData:
    """Generate a sensor update."""

    def __init__(self) -> None:
        """Init sensor data."""
        self._title: str | None = None
        self._precision = _PRECISION_SENTINEL
        self._software_version: str | None = None
        self._device_id_info: dict[str | None, SensorDeviceInfo] = {}
        self._device_id_to_name: dict[str | None, str] = {}
        self._device_id_to_type: dict[str | None, str] = {}

        # Sensors
        self._sensor_descriptions: dict[DeviceKey, SensorDescription] = {}
        self._sensor_descriptions_updates: dict[DeviceKey, SensorDescription] = {}
        self._sensor_values: dict[DeviceKey, SensorValue] = {}
        self._sensor_values_updates: dict[DeviceKey, SensorValue] = {}

        # Binary Sensors
        self._binary_sensor_descriptions: dict[DeviceKey, BinarySensorDescription] = {}
        self._binary_sensor_descriptions_updates: dict[
            DeviceKey, BinarySensorDescription
        ] = {}
        self._binary_sensor_values: dict[DeviceKey, BinarySensorValue] = {}
        self._binary_sensor_values_updates: dict[DeviceKey, BinarySensorValue] = {}

        # Events
        self._events: dict[DeviceKey, Event] = {}
        self._events_updates: dict[DeviceKey, Event] = {}

    @property
    def descriptions(
        self,
    ) -> dict[DeviceKey, SensorDescription]:
        """Return the sensor data."""
        return self._sensor_descriptions

    @property
    def binary_descriptions(
        self,
    ) -> dict[DeviceKey, BinarySensorDescription]:
        """Return the binary sensor data."""
        return self._binary_sensor_descriptions

    @property
    def primary_device_id(self) -> str | None:
        """Return the primary device id."""
        if self._device_id_to_type:
            return list(self._device_id_to_type)[0]
        return None

    @property
    def precision(self) -> int:
        """Return the precision in decimal places."""
        return self._precision

    @property
    def title(self) -> str | None:
        """Return the title."""
        return self._title

    def set_title(self, title: str) -> None:
        """Set the title."""
        self._title = title

    def set_precision(self, precision: int) -> None:
        """Set the precision in decimal places.

        This is a convenience method to have native float values
        rounded to the expected number of decimal places.
        """
        if precision < 0:
            self._precision = _PRECISION_SENTINEL
        self._precision = precision

    def _get_device_info(self, device_id: str | None) -> SensorDeviceInfo:
        """Get device info."""
        if device_id not in self._device_id_info:
            self._device_id_info[device_id] = SensorDeviceInfo(
                None, None, None, None, None
            )
        return self._device_id_info[device_id]

    def set_device_manufacturer(
        self, manufacturer: str, device_id: str | None = None
    ) -> None:
        """Set the device manufacturer."""
        self._get_device_info(device_id).manufacturer = manufacturer

    def set_device_hw_version(
        self, hw_version: str, device_id: str | None = None
    ) -> None:
        """Set the device hardware version."""
        self._get_device_info(device_id).hw_version = hw_version

    def set_device_sw_version(
        self, sw_version: str, device_id: str | None = None
    ) -> None:
        """Set the device software version."""
        self._get_device_info(device_id).sw_version = sw_version

    def set_device_name(self, name: str, device_id: str | None = None) -> None:
        """Set the device name."""
        self._device_id_to_name[device_id] = name
        self._get_device_info(device_id).name = name

    def set_device_type(self, device_type: str, device_id: str | None = None) -> None:
        """Set the device type."""
        self._device_id_to_type[device_id] = device_type
        self._get_device_info(device_id).model = device_type

    @abstractmethod
    def _start_update(self, data: Any) -> None:
        """Update the data."""

    def supported(self, data: Any) -> bool:
        """Return True if the device is supported."""
        self._start_update(data)
        return bool(self._device_id_to_type)

    def update(self, data: Any) -> SensorUpdate:
        """Update a device."""
        # Ensure events from previous
        # updates are not carried over
        # as events are transient.
        self._events_updates.clear()
        self._start_update(data)
        return self._finish_update()

    def _finish_update(self) -> SensorUpdate:
        """Finish the update."""
        self._sensor_descriptions.update(self._sensor_descriptions_updates)
        self._sensor_values.update(self._sensor_values_updates)

        self._binary_sensor_descriptions.update(
            self._binary_sensor_descriptions_updates
        )
        self._binary_sensor_values.update(self._binary_sensor_values_updates)

        return SensorUpdate(
            title=self._title,
            devices=self._device_id_info,
            entity_descriptions=self._sensor_descriptions_updates,
            entity_values=self._sensor_values_updates,
            binary_entity_descriptions=self._binary_sensor_descriptions_updates,
            binary_entity_values=self._binary_sensor_values_updates,
            events=self._events_updates,
        )

    def update_predefined_binary_sensor(
        self,
        device_class: BinarySensorDeviceClass,
        native_value: bool | None,
        key: str | None = None,
        name: str | None = None,
        device_id: str | None = None,
    ) -> None:
        """Update a binary sensor by type."""
        assert device_class is not None  # nosec
        self.update_binary_sensor(
            key=key or device_class.value,
            name=name,
            native_value=native_value,
            device_class=device_class,
            device_id=device_id,
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

    def update_binary_sensor(
        self,
        key: str,
        native_value: bool | None,
        device_class: BinarySensorDeviceClass | None = None,
        name: str | None = None,
        device_id: str | None = None,
    ) -> None:
        """Update a sensor by type."""
        device_key = DeviceKey(key, device_id)
        self._binary_sensor_values_updates[device_key] = BinarySensorValue(
            name=name or self._get_key_name(key, device_id),
            device_key=device_key,
            native_value=native_value,
        )
        self._binary_sensor_descriptions_updates[device_key] = BinarySensorDescription(
            device_key=device_key,
            device_class=device_class,
        )

    def update_sensor(
        self,
        key: str,
        native_unit_of_measurement: Units | None,
        native_value: None | str | int | float | date | datetime | Decimal,
        device_class: SensorDeviceClass | None = None,
        name: str | None = None,
        device_id: str | None = None,
    ) -> None:
        """Update a sensor."""
        device_key = DeviceKey(key, device_id)
        if self.precision != _PRECISION_SENTINEL and isinstance(native_value, float):
            native_value = round(native_value, self.precision)
        self._sensor_values_updates[device_key] = SensorValue(
            name=name or self._get_key_name(key, device_id),
            device_key=device_key,
            native_value=native_value,
        )
        self._sensor_descriptions_updates[device_key] = SensorDescription(
            device_key=device_key,
            native_unit_of_measurement=native_unit_of_measurement,
            device_class=device_class,
        )

    def fire_event(
        self,
        key: str,
        event_type: str,
        event_properties: dict[str, str | int | float | None] | None = None,
        name: str | None = None,
        device_id: str | None = None,
    ) -> None:
        """Fire an event."""
        device_key = DeviceKey(key, device_id)
        self._events_updates[device_key] = Event(
            name=name or self._get_key_name(key, device_id),
            device_key=device_key,
            event_type=event_type,
            event_properties=event_properties,
        )
