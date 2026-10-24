# Supported device classes

from ..base import BaseDeviceClass


class SensorDeviceClass(BaseDeviceClass):
    """Device class for sensors."""

    # absolute humidity (g/m³, mg/m³)
    ABSOLUTE_HUMIDITY = "absolute_humidity"

    # acceleration (mG)
    ACCELERATION = "acceleration"

    # apparent power (VA)
    APPARENT_POWER = "apparent_power"

    # area (m², km², ft², ac, ha, ...)
    AREA = "area"

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

    # data rate (bit/s, kB/s, MB/s, ...)
    DATA_RATE = "data_rate"

    # data size (bit, B, kB, MB, ...)
    DATA_SIZE = "data_size"

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

    # energy per distance (kWh/100km, Wh/km, mi/kWh, km/kWh)
    ENERGY_DISTANCE = "energy_distance"

    # stored energy (Wh, kWh, MWh, J, ...)
    ENERGY_STORAGE = "energy_storage"

    # enumeration: state is one of a fixed list of options (no unit)
    ENUM = "enum"

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

    # weight, i.e. an object's mass (μg, mg, g, kg, oz, lb)
    WEIGHT = "weight"

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

    # potential hydrogen, acidity/alkalinity (no unit)
    PH = "ph"

    # Packet id (no unit)
    PACKET_ID = "packet_id"

    # Particulate matter <= 0.1 μm (µg/m³)
    PM1 = "pm1"

    # Particulate matter <= 10 μm (µg/m³)
    PM10 = "pm10"

    # Particulate matter <= 2.5 μm (µg/m³)
    PM25 = "pm25"

    # Particulate matter <= 4 μm (µg/m³)
    PM4 = "pm4"

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

    # radon concentration (Bq/m³, pCi/L)
    RADON = "radon"

    # reactive energy (varh, kvarh)
    REACTIVE_ENERGY = "reactive_energy"

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

    # temperature difference (°C, °F, K)
    TEMPERATURE_DELTA = "temperature_delta"

    # time (s)
    TIME = "time"

    # timestamp (ISO8601)
    TIMESTAMP = "timestamp"

    # uptime: when the device last restarted (ISO8601)
    UPTIME = "uptime"

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

    # stored volume, e.g. fuel in a tank (mL, L, m³, gal, ...)
    VOLUME_STORAGE = "volume_storage"

    # wind direction (°)
    WIND_DIRECTION = "wind_direction"

    # Water (L)
    WATER = "water"
