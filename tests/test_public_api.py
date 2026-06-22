"""Public API surface contract."""

import sensor_state_data
from sensor_state_data import (
    BaseBinarySensorDescription,
    BaseDescription,
    BaseSensorDescription,
    SensorLibrary,
)


def test_base_description_classes_importable_from_root():
    """Base description classes are part of the public API."""
    assert issubclass(BaseSensorDescription, BaseDescription)
    assert issubclass(BaseBinarySensorDescription, BaseDescription)


def test_sensor_library_entries_are_base_sensor_descriptions():
    """SensorLibrary exposes BaseSensorDescription instances, so the class
    must be importable from the package root to annotate/check them."""
    entry = SensorLibrary.BATTERY__PERCENTAGE
    assert isinstance(entry, BaseSensorDescription)


def test_all_names_are_importable():
    """Every name in __all__ resolves to a real attribute."""
    for name in sensor_state_data.__all__:
        assert hasattr(sensor_state_data, name), name
