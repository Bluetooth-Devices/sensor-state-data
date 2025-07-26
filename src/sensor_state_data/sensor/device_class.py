# Supported device classes

from ..base import BaseDeviceClass


class SensorDeviceClass(BaseDeviceClass):
    """Device class for sensors."""

    # acceleration (mG)
    ACCELERATION = "acceleration"

    # apparent power (VA)
    APPARENT_POWER = "apparent_power"

    # Air Quality Index
    AQI = "aqi"

    # % of battery that is left
    BATTERY = "battery"

    # ppm (parts per million) Carbon Monoxide gas concentration
    CO = "carbon_monoxide"

    # ppm (parts per million) Carbon Dioxide gas concentration
    CO2 = "carbon_dioxide"

    # conductivity (µS/cm)
    CONDUCTIVITY = "conductivity"

    # count (no unit)
    COUNT = "count"

    # current (A)
    CURRENT = "current"

    # date (ISO8601)
    DATE = "date"

    # dew point (°C, F)
    DEW_POINT = "dew_point"

    # distance (mm, m)
    DISTANCE = "distance"

    # fixed duration (TIME_DAYS, TIME_HOURS, TIME_MINUTES, TIME_SECONDS)
    DURATION = "duration"

    # energy (Wh, kWh, MWh)
    ENERGY = "energy"

    # Volume flow rate (m3 per hour)
    VOLUME_FLOW_RATE = "volume_flow_rate"

    # formaldehyde (µg/m³)
    FORMALDEHYDE = "formaldehyde"

    # frequency (Hz, kHz, MHz, GHz)
    FREQUENCY = "frequency"

    # gas (m³ or ft³)
    GAS = "gas"

    # gyroscope (° per second)
    GYROSCOPE = "gyroscope"

    # % of humidity in the air
    HUMIDITY = "humidity"

    # current light level (lx/lm)
    ILLUMINANCE = "illuminance"

    # impedance (Ohm)
    IMPEDANCE = "impedance"

    # keg size (L)
    KEG_SIZE = "keg_size"

    # keg type (no unit)
    KEG_TYPE = "keg_type"

    # % of moisture in the air or soil
    MOISTURE = "moisture"

    # mass (g, kg, lbs)
    MASS = "mass"

    # mass non-stabilized (kg/lbs)
    MASS_NON_STABILIZED = "mass_non_stabilized"

    # Amount of money (currency)
    MONETARY = "monetary"

    # Amount of NO2 (µg/m³)
    NITROGEN_DIOXIDE = "nitrogen_dioxide"

    # Amount of NO (µg/m³)
    NITROGEN_MONOXIDE = "nitrogen_monoxide"

    # Amount of N2O  (µg/m³)
    NITROUS_OXIDE = "nitrous_oxide"

    # Amount of O3 (µg/m³)
    OZONE = "ozone"

    # Packet id (no unit)
    PACKET_ID = "packet_id"

    # Particulate matter <= 0.1 μm (µg/m³)
    PM1 = "pm1"

    # Particulate matter <= 10 μm (µg/m³)
    PM10 = "pm10"

    # Particulate matter <= 2.5 μm (µg/m³)
    PM25 = "pm25"

    # Port count (no unit)
    PORT_COUNT = "port_count"

    # Port name (no unit)
    PORT_NAME = "port_name"

    # Port state (no unit)
    PORT_STATE = "port_state"

    # power factor (%)
    POWER_FACTOR = "power_factor"

    # power (W/kW)
    POWER = "power"

    # pressure (hPa/mbar)
    PRESSURE = "pressure"

    # rotation (°)
    ROTATION = "rotation"

    # reactive power (var)
    REACTIVE_POWER = "reactive_power"

    # signal strength (dB/dBm)
    SIGNAL_STRENGTH = "signal_strength"

    # specific gravity
    SPECIFIC_GRAVITY = "specific_gravity"

    # speed (m/s)
    SPEED = "speed"

    # Amount of SO2 (µg/m³)
    SULPHUR_DIOXIDE = "sulphur_dioxide"

    # temperature (°C/F)
    TEMPERATURE = "temperature"

    # time (s)
    TIME = "time"

    # timestamp (ISO8601)
    TIMESTAMP = "timestamp"

    # UV index (no unit)
    UV_INDEX = "uv_index"

    # Amount of VOC (µg/m³)
    VOLATILE_ORGANIC_COMPOUNDS = "volatile_organic_compounds"

    # voltage (V)
    VOLTAGE = "voltage"

    # Volume (ml, L)
    VOLUME = "volume"

    # Volume dispensed (L)
    VOLUME_DISPENSED = "volume_dispensed"

    # Volume start (L)
    VOLUME_START = "volume_start"

    # Water (L)
    WATER = "water"
