from typing import Any

from sensor_state_data import (
    DeviceClass,
    DeviceKey,
    SensorData,
    SensorDescription,
    SensorDeviceClass,
    SensorLibrary,
    SensorUpdate,
    SensorValue,
    Units,
)


def test_device_class():
    assert DeviceClass.TEMPERATURE == "temperature"
    assert str(DeviceClass.TEMPERATURE) == "temperature"


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
    )
