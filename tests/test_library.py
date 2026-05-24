"""Behavioral coverage for the air-quality SensorLibrary descriptions.

These device classes already existed in SensorDeviceClass but had no
SensorLibrary convenience description, unlike FORMALDEHYDE and
VOLATILE_ORGANIC_COMPOUNDS in the same concentration family. The tests assert
on the observable SensorUpdate produced through update_predefined_sensor rather
than inspecting the constants directly.
"""

from typing import Any

import pytest

from sensor_state_data import (
    DeviceKey,
    SensorData,
    SensorDescription,
    SensorDeviceClass,
    SensorLibrary,
    SensorValue,
    Units,
)
from sensor_state_data.description import BaseSensorDescription

# (library constant, expected device class, expected unit)
AIR_QUALITY_DESCRIPTIONS = [
    (
        SensorLibrary.CO__CONCENTRATION_PARTS_PER_MILLION,
        SensorDeviceClass.CO,
        Units.CONCENTRATION_PARTS_PER_MILLION,
    ),
    (
        SensorLibrary.NITROGEN_DIOXIDE__CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        SensorDeviceClass.NITROGEN_DIOXIDE,
        Units.CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    ),
    (
        SensorLibrary.NITROGEN_MONOXIDE__CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        SensorDeviceClass.NITROGEN_MONOXIDE,
        Units.CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    ),
    (
        SensorLibrary.NITROUS_OXIDE__CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        SensorDeviceClass.NITROUS_OXIDE,
        Units.CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    ),
    (
        SensorLibrary.OZONE__CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        SensorDeviceClass.OZONE,
        Units.CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    ),
    (
        SensorLibrary.SULPHUR_DIOXIDE__CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        SensorDeviceClass.SULPHUR_DIOXIDE,
        Units.CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    ),
]


@pytest.mark.parametrize(
    ("description", "device_class", "unit"), AIR_QUALITY_DESCRIPTIONS
)
def test_air_quality_description_metadata(
    description: BaseSensorDescription,
    device_class: SensorDeviceClass,
    unit: Units,
) -> None:
    """Each air-quality constant carries its device class and unit."""
    assert description.device_class is device_class
    assert description.native_unit_of_measurement is unit


@pytest.mark.parametrize(
    ("description", "device_class", "unit"), AIR_QUALITY_DESCRIPTIONS
)
def test_air_quality_description_flows_through_update(
    description: BaseSensorDescription,
    device_class: SensorDeviceClass,
    unit: Units,
) -> None:
    """update_predefined_sensor emits the expected description and value."""

    class MySensorData(SensorData):
        def _start_update(self, data: Any) -> None:
            self.update_predefined_sensor(description, 12.0)

    update = MySensorData().update(b"")
    key = DeviceKey(key=device_class.value, device_id=None)

    assert update.entity_descriptions[key] == SensorDescription(
        device_key=key,
        device_class=device_class,
        native_unit_of_measurement=unit,
    )
    assert update.entity_values[key] == SensorValue(
        device_key=key,
        name=device_class.value.replace("_", " ").title(),
        native_value=12.0,
    )
