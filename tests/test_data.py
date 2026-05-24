"""Behavioral coverage for the SensorData public API.

test_init.py already exercises precision rounding and events. These tests cover
the rest of the public surface that was previously untested: title, device
info aggregation, binary sensors, supported(), primary_device_id and
get_device_name. They assert on observable outputs (the returned SensorUpdate,
property values, return values) rather than internal state.
"""

from typing import Any

from sensor_state_data import (
    BinarySensorDeviceClass,
    BinarySensorValue,
    DeviceKey,
    SensorData,
    SensorDeviceInfo,
    SensorLibrary,
)
from sensor_state_data.description import BinarySensorDescription


def test_title_is_reported_in_update():
    class MySensorData(SensorData):
        def _start_update(self, data: Any) -> None:
            self.set_title("Living Room Sensor")
            self.update_predefined_sensor(SensorLibrary.TEMPERATURE__CELSIUS, 21.0)

    data = MySensorData()
    update = data.update(b"")

    assert data.title == "Living Room Sensor"
    assert update.title == "Living Room Sensor"


def test_device_info_is_aggregated_per_device():
    class MySensorData(SensorData):
        def _start_update(self, data: Any) -> None:
            self.set_device_name("Thermometer", device_id="aa")
            self.set_device_type("Sensirion", device_id="aa")
            self.set_device_manufacturer("Sensirion AG", device_id="aa")
            self.set_device_hw_version("1.0", device_id="aa")
            self.set_device_sw_version("2.3", device_id="aa")

    data = MySensorData()
    update = data.update(b"")

    assert update.devices == {
        "aa": SensorDeviceInfo(
            name="Thermometer",
            model="Sensirion",
            manufacturer="Sensirion AG",
            sw_version="2.3",
            hw_version="1.0",
        )
    }


def test_multiple_devices_tracked_independently():
    class MySensorData(SensorData):
        def _start_update(self, data: Any) -> None:
            self.set_device_type("Outdoor", device_id="aa")
            self.set_device_type("Indoor", device_id="bb")

    data = MySensorData()
    update = data.update(b"")

    assert set(update.devices) == {"aa", "bb"}
    assert update.devices["aa"].model == "Outdoor"
    assert update.devices["bb"].model == "Indoor"


def test_primary_device_id_is_first_registered_type():
    class MySensorData(SensorData):
        def _start_update(self, data: Any) -> None:
            self.set_device_type("Outdoor", device_id="aa")
            self.set_device_type("Indoor", device_id="bb")

    data = MySensorData()
    data.update(b"")

    assert data.primary_device_id == "aa"


def test_primary_device_id_is_none_without_devices():
    data = SensorData()

    assert data.primary_device_id is None


def test_get_device_name_prefers_name_over_type():
    class MySensorData(SensorData):
        def _start_update(self, data: Any) -> None:
            self.set_device_type("Sensirion", device_id="aa")
            self.set_device_name("Bedroom", device_id="aa")

    data = MySensorData()
    data.update(b"")

    assert data.get_device_name("aa") == "Bedroom"


def test_get_device_name_falls_back_to_type():
    class MySensorData(SensorData):
        def _start_update(self, data: Any) -> None:
            self.set_device_type("Sensirion", device_id="aa")

    data = MySensorData()
    data.update(b"")

    assert data.get_device_name("aa") == "Sensirion"


def test_get_device_name_unknown_device_is_none():
    data = SensorData()

    assert data.get_device_name("missing") is None


def test_supported_true_when_device_type_set():
    class MySensorData(SensorData):
        def _start_update(self, data: Any) -> None:
            self.set_device_type("Sensirion", device_id="aa")

    assert MySensorData().supported(b"") is True


def test_supported_false_without_device_type():
    class MySensorData(SensorData):
        def _start_update(self, data: Any) -> None:
            # Reports a value but never declares a device type.
            self.update_predefined_sensor(SensorLibrary.TEMPERATURE__CELSIUS, 21.0)

    assert MySensorData().supported(b"") is False


def test_update_binary_sensor_emits_value_and_description():
    class MySensorData(SensorData):
        def _start_update(self, data: Any) -> None:
            self.update_binary_sensor(
                key="motion",
                native_value=True,
                device_class=BinarySensorDeviceClass.MOTION,
            )

    data = MySensorData()
    update = data.update(b"")
    device_key = DeviceKey(key="motion", device_id=None)

    assert update.binary_entity_values == {
        device_key: BinarySensorValue(
            device_key=device_key,
            name="Motion",
            native_value=True,
        )
    }
    assert update.binary_entity_descriptions == {
        device_key: BinarySensorDescription(
            device_key=device_key,
            device_class=BinarySensorDeviceClass.MOTION,
        )
    }


def test_update_predefined_binary_sensor_defaults_key_to_device_class():
    class MySensorData(SensorData):
        def _start_update(self, data: Any) -> None:
            self.update_predefined_binary_sensor(
                BinarySensorDeviceClass.OCCUPANCY, False
            )

    data = MySensorData()
    update = data.update(b"")
    device_key = DeviceKey(key="occupancy", device_id=None)

    assert update.binary_entity_values[device_key].native_value is False
    assert (
        update.binary_entity_descriptions[device_key].device_class
        is BinarySensorDeviceClass.OCCUPANCY
    )


def test_device_id_propagates_into_device_key():
    class MySensorData(SensorData):
        def _start_update(self, data: Any) -> None:
            self.update_predefined_sensor(
                SensorLibrary.TEMPERATURE__CELSIUS, 21.0, device_id="aa"
            )

    data = MySensorData()
    update = data.update(b"")

    assert DeviceKey(key="temperature", device_id="aa") in update.entity_values


def test_descriptions_accumulate_across_updates():
    class MySensorData(SensorData):
        def _start_update(self, data: Any) -> None:
            self.update_predefined_sensor(SensorLibrary.TEMPERATURE__CELSIUS, 21.0)

    data = MySensorData()
    data.update(b"")
    data.update(b"")

    # The persistent `descriptions` property retains the sensor across updates.
    assert DeviceKey(key="temperature", device_id=None) in data.descriptions


def test_events_do_not_persist_between_updates():
    class MySensorData(SensorData):
        def _start_update(self, data: Any) -> None:
            if data == b"fire":
                self.fire_event(key="button", event_type="press")

    data = MySensorData()
    first = data.update(b"fire")
    second = data.update(b"")

    assert DeviceKey(key="button", device_id=None) in first.events
    assert second.events == {}


def test_returned_update_events_are_an_immutable_snapshot():
    """A returned SensorUpdate must keep its events when a later update() runs.

    Regression guard: _finish_update() used to return the live _events_updates
    dict by reference, and the next update() called .clear() on it — mutating an
    already-returned (frozen) SensorUpdate out from under the caller.
    """

    class MySensorData(SensorData):
        def _start_update(self, data: Any) -> None:
            if data == b"fire":
                self.fire_event(key="button", event_type="press")

    data = MySensorData()
    first = data.update(b"fire")
    data.update(b"")  # second update must not touch `first`

    assert DeviceKey(key="button", device_id=None) in first.events


def test_returned_update_values_are_an_immutable_snapshot():
    """Values in a returned SensorUpdate must not change when a later update() runs.

    Regression guard: the per-update value/description dicts were returned by
    reference and reused across updates, so holding an earlier SensorUpdate and
    reading it after a later update() yielded the newer value.
    """

    class MySensorData(SensorData):
        def _start_update(self, data: Any) -> None:
            self.update_predefined_sensor(
                SensorLibrary.TEMPERATURE__CELSIUS, float(len(data))
            )

    data = MySensorData()
    key = DeviceKey(key="temperature", device_id=None)

    first = data.update(b"aaaa")  # temperature == 4.0
    assert first.entity_values[key].native_value == 4.0

    data.update(b"aa")  # temperature == 2.0; must not rewrite `first`
    assert first.entity_values[key].native_value == 4.0
