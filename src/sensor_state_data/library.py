from __future__ import annotations

from .description import BaseSensorDescription
from .device_class import DeviceClass
from .units import Units


class SensorLibrary:
    """A library of sensor common descriptions."""

    TEMPERATURE__CELSIUS = BaseSensorDescription(
        device_class=DeviceClass.TEMPERATURE,
        native_unit_of_measurement=Units.TEMP_CELSIUS,
    )
    PRESSURE__MBAR = BaseSensorDescription(
        device_class=DeviceClass.PRESSURE,
        native_unit_of_measurement=Units.PRESSURE_MBAR,
    )
    HUMIDITY__PERCENTAGE = BaseSensorDescription(
        device_class=DeviceClass.HUMIDITY, native_unit_of_measurement=Units.PERCENTAGE
    )
    LIGHT__LIGHT_LUX = BaseSensorDescription(
        device_class=DeviceClass.ILLUMINANCE, native_unit_of_measurement=Units.LIGHT_LUX
    )
    VOLTAGE__ELECTRIC_POTENTIAL_VOLT = BaseSensorDescription(
        device_class=DeviceClass.VOLTAGE,
        native_unit_of_measurement=Units.ELECTRIC_POTENTIAL_VOLT,
    )
    CURRENT__POWER_VOLT_AMPERE = BaseSensorDescription(
        device_class=DeviceClass.CURRENT,
        native_unit_of_measurement=Units.POWER_VOLT_AMPERE,
    )
    POWER__POWER_WATT = BaseSensorDescription(
        device_class=DeviceClass.POWER, native_unit_of_measurement=Units.POWER_WATT
    )
    BATTERY__PERCENTAGE = BaseSensorDescription(
        device_class=DeviceClass.BATTERY, native_unit_of_measurement=Units.PERCENTAGE
    )
