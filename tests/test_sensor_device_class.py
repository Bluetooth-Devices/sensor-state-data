from sensor_state_data import SensorDeviceClass


def test_particulate_matter_device_class_values():
    """Pin the particulate-matter device class identifiers.

    These string values are the interop contract with Home Assistant:
    a consumer matches entities on ``device_class.value``. A typo or an
    accidental rename here silently breaks that matching, so lock the
    PM family (each suffix is the upper size bound in micrometers).
    """
    assert SensorDeviceClass.PM1 == "pm1"
    assert SensorDeviceClass.PM4 == "pm4"
    assert SensorDeviceClass.PM10 == "pm10"
    assert SensorDeviceClass.PM25 == "pm25"


def test_sensor_device_class_str_returns_value():
    """A SensorDeviceClass stringifies to its bare value (StrEnum contract)."""
    assert str(SensorDeviceClass.PM1) == "pm1"  # type: ignore[unreachable]
