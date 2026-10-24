"""Pin the string values of the weather/environmental sensor device classes.

These strings are the Home Assistant interop contract — changing them silently
breaks consumers that compare device classes by value, so they are pinned here.
"""

from sensor_state_data import SensorDeviceClass


def test_weather_device_class_values():
    assert SensorDeviceClass.ATMOSPHERIC_PRESSURE.value == "atmospheric_pressure"
    assert SensorDeviceClass.IRRADIANCE.value == "irradiance"
    assert SensorDeviceClass.PRECIPITATION.value == "precipitation"
    assert SensorDeviceClass.PRECIPITATION_INTENSITY.value == "precipitation_intensity"
    assert SensorDeviceClass.WIND_SPEED.value == "wind_speed"


def test_weather_device_class_str():
    # StrEnum: str() returns the value, not "SensorDeviceClass.WIND_SPEED"
    assert str(SensorDeviceClass.WIND_SPEED) == "wind_speed"


def test_atmospheric_pressure_distinct_from_pressure():
    assert SensorDeviceClass.ATMOSPHERIC_PRESSURE != SensorDeviceClass.PRESSURE
