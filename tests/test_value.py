"""Tests for the value/device dataclasses, including their slotted layout."""

from __future__ import annotations

import pytest

from sensor_state_data import (
    BinarySensorValue,
    DeviceKey,
    Event,
    SensorValue,
)

SLOTTED_CLASSES = [DeviceKey, SensorValue, BinarySensorValue, Event]


@pytest.fixture
def device_key() -> DeviceKey:
    return DeviceKey(key="temperature", device_id="dev1")


@pytest.mark.parametrize("cls", SLOTTED_CLASSES)
def test_classes_define_slots(cls: type) -> None:
    """Each value dataclass declares __slots__ so instances carry no __dict__."""
    assert hasattr(cls, "__slots__")


def test_instances_have_no_dict(device_key: DeviceKey) -> None:
    """Slotted instances do not allocate a per-instance __dict__."""
    sensor = SensorValue(device_key=device_key, name="Temp", native_value=21.5)
    binary = BinarySensorValue(device_key=device_key, name="Motion", native_value=True)
    event = Event(
        device_key=device_key,
        name="Motion",
        event_type="motion_detected",
        event_properties=None,
    )
    for obj in (device_key, sensor, binary, event):
        assert not hasattr(obj, "__dict__")


def test_instances_remain_frozen(device_key: DeviceKey) -> None:
    """slots=True does not break frozen immutability."""
    sensor = SensorValue(device_key=device_key, name="Temp", native_value=21.5)
    with pytest.raises(Exception):  # FrozenInstanceError
        sensor.native_value = 0  # type: ignore[misc]


def test_equality_and_hash_preserved() -> None:
    """Value semantics (eq/hash) survive the slotted layout."""
    a = DeviceKey(key="temperature", device_id="dev1")
    b = DeviceKey(key="temperature", device_id="dev1")
    assert a == b
    assert hash(a) == hash(b)

    s1 = SensorValue(device_key=a, name="Temp", native_value=21.5)
    s2 = SensorValue(device_key=b, name="Temp", native_value=21.5)
    assert s1 == s2


def test_field_values_round_trip(device_key: DeviceKey) -> None:
    """Constructed fields are readable and unchanged."""
    event = Event(
        device_key=device_key,
        name="Button",
        event_type="press",
        event_properties={"count": 2},
    )
    assert event.device_key is device_key
    assert event.name == "Button"
    assert event.event_type == "press"
    assert event.event_properties == {"count": 2}
