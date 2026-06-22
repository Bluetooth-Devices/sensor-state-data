"""Pin the HA interop string values for recently added sensor device classes.

These string values are the contract with Home Assistant. They must match HA's
``SensorDeviceClass`` exactly, so drift is caught here rather than downstream.
"""

from sensor_state_data import SensorDeviceClass


def test_blood_glucose_concentration_value():
    assert (
        SensorDeviceClass.BLOOD_GLUCOSE_CONCENTRATION == "blood_glucose_concentration"
    )


def test_sound_pressure_value():
    assert SensorDeviceClass.SOUND_PRESSURE == "sound_pressure"


def test_volatile_organic_compounds_parts_value():
    assert (
        SensorDeviceClass.VOLATILE_ORGANIC_COMPOUNDS_PARTS
        == "volatile_organic_compounds_parts"
    )
