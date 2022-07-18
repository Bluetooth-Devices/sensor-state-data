from __future__ import annotations

from enum import Enum

from .description import SensorDescription
from .device_class import DeviceClass
from .units import (
    ELECTRIC_POTENTIAL_VOLT,
    LIGHT_LUX,
    PERCENTAGE,
    POWER_VOLT_AMPERE,
    POWER_WATT,
    PRESSURE_PA,
    TEMP_CELSIUS,
)


class SensorLibrary(Enum):

    TEMPERATURE = SensorDescription(
        device_class=DeviceClass.TEMPERATURE, native_unit_of_measurement=TEMP_CELSIUS
    )
    PRESSURE = SensorDescription(
        device_class=DeviceClass.PRESSURE, native_unit_of_measurement=PRESSURE_PA
    )
    HUMIDITY = SensorDescription(
        device_class=DeviceClass.HUMIDITY, native_unit_of_measurement=PERCENTAGE
    )
    LIGHT = SensorDescription(
        device_class=DeviceClass.ILLUMINANCE, native_unit_of_measurement=LIGHT_LUX
    )
    VOLTAGE = SensorDescription(
        device_class=DeviceClass.VOLTAGE,
        native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
    )
    CURRENT = SensorDescription(
        device_class=DeviceClass.CURRENT, native_unit_of_measurement=POWER_VOLT_AMPERE
    )
    POWER = SensorDescription(
        device_class=DeviceClass.POWER, native_unit_of_measurement=POWER_WATT
    )
    BATTERY = SensorDescription(
        device_class=DeviceClass.BATTERY, native_unit_of_measurement=PERCENTAGE
    )
