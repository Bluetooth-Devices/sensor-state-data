"""Pin the HA interop string values for device classes added for HA parity.

These string values are the contract with Home Assistant. They must match HA's
``SensorDeviceClass`` / ``BinarySensorDeviceClass`` exactly, so drift is caught
here rather than downstream.
"""

import pytest

from sensor_state_data import BinarySensorDeviceClass, SensorDeviceClass


@pytest.mark.parametrize(
    ("name", "value"),
    [
        ("ABSOLUTE_HUMIDITY", "absolute_humidity"),
        ("AREA", "area"),
        ("DATA_RATE", "data_rate"),
        ("DATA_SIZE", "data_size"),
        ("ENERGY_DISTANCE", "energy_distance"),
        ("ENERGY_STORAGE", "energy_storage"),
        ("ENUM", "enum"),
        ("PH", "ph"),
        ("RADON", "radon"),
        ("REACTIVE_ENERGY", "reactive_energy"),
        ("TEMPERATURE_DELTA", "temperature_delta"),
        ("UPTIME", "uptime"),
        ("VOLUME_STORAGE", "volume_storage"),
        ("WEIGHT", "weight"),
        ("WIND_DIRECTION", "wind_direction"),
    ],
)
def test_sensor_device_class_value(name: str, value: str) -> None:
    member = SensorDeviceClass[name]
    assert member == value
    assert SensorDeviceClass(value) is member


def test_glass_break_value() -> None:
    assert BinarySensorDeviceClass("glass_break") is BinarySensorDeviceClass.GLASS_BREAK
    assert BinarySensorDeviceClass.GLASS_BREAK == "glass_break"
