from typing import Any

from sensor_state_data import (
    BinarySensorDeviceClass,
    DeviceClass,
    DeviceKey,
    Event,
    EventDeviceKeys,
    EventTypes,
    SensorData,
    SensorDescription,
    SensorDeviceClass,
    SensorLibrary,
    SensorUpdate,
    SensorValue,
    Units,
)


def test_sensor_device_class():
    assert DeviceClass.TEMPERATURE == "temperature"
    assert str(DeviceClass.TEMPERATURE) == "temperature"


def test_binary_sensor_device_class():
    assert BinarySensorDeviceClass.POWER == "power"
    assert str(BinarySensorDeviceClass.POWER) == "power"


def test_event_device_keys():
    assert EventDeviceKeys.SWITCH == "switch"
    assert str(EventDeviceKeys.SWITCH) == "switch"


def test_event_types():
    assert EventTypes.TURN_ON == "turn_on"
    assert str(EventTypes.TURN_ON) == "turn_on"


def test_no_precision():
    class MySensorData(SensorData):
        def _start_update(self, data: Any) -> None:
            self.update_predefined_sensor(
                SensorLibrary.TEMPERATURE__CELSIUS, 30.3232039
            )

    data = MySensorData()

    update = data.update(b"")
    assert update == SensorUpdate(
        title=None,
        devices={},
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            )
        },
        entity_values={
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=30.3232039,
            )
        },
        binary_entity_descriptions={},
        binary_entity_values={},
        events={},
    )


def test_with_precision():
    class MySensorData(SensorData):
        def _start_update(self, data: Any) -> None:
            self.set_precision(2)
            self.update_predefined_sensor(
                SensorLibrary.TEMPERATURE__CELSIUS, 30.3232039
            )

    data = MySensorData()

    update = data.update(b"")
    assert update == SensorUpdate(
        title=None,
        devices={},
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            )
        },
        entity_values={
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=30.32,
            )
        },
        binary_entity_descriptions={},
        binary_entity_values={},
        events={},
    )


def test_with_precision_between_updates():
    class MySensorData(SensorData):
        def _start_update(self, data: Any) -> None:
            self.set_precision(2)
            self.update_predefined_sensor(
                SensorLibrary.TEMPERATURE__CELSIUS, 30.3232039
            )
            self.set_precision(4)
            self.update_predefined_sensor(
                SensorLibrary.TEMPERATURE__CELSIUS, 30.3232039
            )

    data = MySensorData()

    update = data.update(b"")
    assert update == SensorUpdate(
        title=None,
        devices={},
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            )
        },
        entity_values={
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=30.3232,
            )
        },
        binary_entity_descriptions={},
        binary_entity_values={},
        events={},
    )


def test_with_precision_does_not_add_trailing_zeros():
    class MySensorData(SensorData):
        def _start_update(self, data: Any) -> None:
            self.set_precision(2)
            self.update_predefined_sensor(SensorLibrary.TEMPERATURE__CELSIUS, 30.9999)
            self.update_predefined_sensor(SensorLibrary.HUMIDITY__PERCENTAGE, 30)

    data = MySensorData()

    update = data.update(b"")
    assert update == SensorUpdate(
        title=None,
        devices={},
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
        },
        entity_values={
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=31.0,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=30,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
        events={},
    )

def test_event():
    class MySensorData(SensorData):
        def _start_update(self, data: Any) -> None:
            self.update_event(
                key=EventDeviceKeys.DIMMER,
                event_type=EventTypes.ROTATE_LEFT,
                event_subtype=3,
                device_id="living_room"
            )

    data = MySensorData()

    update = data.update(b"")
    assert update == SensorUpdate(
        title=None,
        devices={},
        entity_descriptions={},
        entity_values={},
        binary_entity_descriptions={},
        binary_entity_values={},
        events={
            DeviceKey(key="dimmer", device_id="living_room"): Event(
                device_key=DeviceKey(key="dimmer", device_id="living_room"),
                name="Dimmer",
                event_type="rotate_left",
                event_subtype=3,
            )
        },
    )
