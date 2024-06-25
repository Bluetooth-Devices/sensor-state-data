import pytest

from sensor_state_data.enum import StrEnum


def test_non_str():
    with pytest.raises(TypeError):

        class DeviceClass(StrEnum):
            X = 1
