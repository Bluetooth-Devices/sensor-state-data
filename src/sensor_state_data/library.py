from __future__ import annotations

from .description import BaseSensorDescription
from .sensor.device_class import SensorDeviceClass
from .units import Units


class SensorLibrary:
    """A library of sensor common descriptions."""

    TEMPERATURE__CELSIUS = BaseSensorDescription(
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=Units.TEMP_CELSIUS,
    )
    PRESSURE__MBAR = BaseSensorDescription(
        device_class=SensorDeviceClass.PRESSURE,
        native_unit_of_measurement=Units.PRESSURE_MBAR,
    )
    HUMIDITY__PERCENTAGE = BaseSensorDescription(
        device_class=SensorDeviceClass.HUMIDITY,
        native_unit_of_measurement=Units.PERCENTAGE,
    )
    LIGHT__LIGHT_LUX = BaseSensorDescription(
        device_class=SensorDeviceClass.ILLUMINANCE,
        native_unit_of_measurement=Units.LIGHT_LUX,
    )
    VOLTAGE__ELECTRIC_POTENTIAL_VOLT = BaseSensorDescription(
        device_class=SensorDeviceClass.VOLTAGE,
        native_unit_of_measurement=Units.ELECTRIC_POTENTIAL_VOLT,
    )
    CURRENT__POWER_VOLT_AMPERE = BaseSensorDescription(
        device_class=SensorDeviceClass.CURRENT,
        native_unit_of_measurement=Units.POWER_VOLT_AMPERE,
    )
    POWER__POWER_WATT = BaseSensorDescription(
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=Units.POWER_WATT,
    )
    ENERGY__ENERGY_KILO_WATT_HOUR = BaseSensorDescription(
        device_class=SensorDeviceClass.ENERGY,
        native_unit_of_measurement=Units.ENERGY_KILO_WATT_HOUR,
    )
    GAS__VOLUME_CUBIC_METERS = BaseSensorDescription(
        device_class=SensorDeviceClass.GAS,
        native_unit_of_measurement=Units.VOLUME_CUBIC_METERS,
    )
    BATTERY__PERCENTAGE = BaseSensorDescription(
        device_class=SensorDeviceClass.BATTERY,
        native_unit_of_measurement=Units.PERCENTAGE,
    )
    PM1 = BaseSensorDescription(
        device_class=SensorDeviceClass.PM1,
        native_unit_of_measurement=Units.CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    )
    PM10 = BaseSensorDescription(
        device_class=SensorDeviceClass.PM10,
        native_unit_of_measurement=Units.CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    )
    PM25 = BaseSensorDescription(
        device_class=SensorDeviceClass.PM25,
        native_unit_of_measurement=Units.CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    )
    PM1__CONCENTRATION_MICROGRAMS_PER_CUBIC_METER = BaseSensorDescription(
        device_class=SensorDeviceClass.PM1,
        native_unit_of_measurement=Units.CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    )
    PM10__CONCENTRATION_MICROGRAMS_PER_CUBIC_METER = BaseSensorDescription(
        device_class=SensorDeviceClass.PM10,
        native_unit_of_measurement=Units.CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    )
    PM25__CONCENTRATION_MICROGRAMS_PER_CUBIC_METER = BaseSensorDescription(
        device_class=SensorDeviceClass.PM25,
        native_unit_of_measurement=Units.CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    )
    CO2__CONCENTRATION_PARTS_PER_MILLION = BaseSensorDescription(
        device_class=SensorDeviceClass.CO2,
        native_unit_of_measurement=Units.CONCENTRATION_PARTS_PER_MILLION,
    )
    VOLATILE_ORGANIC_COMPOUNDS__CONCENTRATION_PARTS_PER_MILLION = BaseSensorDescription(
        device_class=SensorDeviceClass.VOLATILE_ORGANIC_COMPOUNDS,
        native_unit_of_measurement=Units.CONCENTRATION_PARTS_PER_MILLION,
    )
