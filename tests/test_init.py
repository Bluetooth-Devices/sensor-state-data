from sensor_state_data import DeviceClass


def test_device_class():
    assert DeviceClass.TEMPERATURE == "temperature"
    assert str(DeviceClass.TEMPERATURE) == "temperature"
