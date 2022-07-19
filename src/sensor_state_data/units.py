from __future__ import annotations

from typing import Final

# These are currently the same as Home Assistant sensors

# #### UNITS OF MEASUREMENT ####
# Apparent power units
POWER_VOLT_AMPERE: Final = "VA"

# Power units
POWER_WATT: Final = "W"
POWER_KILO_WATT: Final = "kW"
POWER_BTU_PER_HOUR: Final = "BTU/h"

# Reactive power units
POWER_VOLT_AMPERE_REACTIVE: Final = "var"

# Energy units
ENERGY_WATT_HOUR: Final = "Wh"
ENERGY_KILO_WATT_HOUR: Final = "kWh"
ENERGY_MEGA_WATT_HOUR: Final = "MWh"

# Electric_current units
ELECTRIC_CURRENT_MILLIAMPERE: Final = "mA"
ELECTRIC_CURRENT_AMPERE: Final = "A"

# Electric_potential units
ELECTRIC_POTENTIAL_MILLIVOLT: Final = "mV"
ELECTRIC_POTENTIAL_VOLT: Final = "V"

# Degree units
DEGREE: Final = "°"

# Currency units
CURRENCY_EURO: Final = "€"
CURRENCY_DOLLAR: Final = "$"
CURRENCY_CENT: Final = "¢"

# Temperature units
TEMP_CELSIUS: Final = "°C"
TEMP_FAHRENHEIT: Final = "°F"
TEMP_KELVIN: Final = "K"

# Time units
TIME_MICROSECONDS: Final = "μs"
TIME_MILLISECONDS: Final = "ms"
TIME_SECONDS: Final = "s"
TIME_MINUTES: Final = "min"
TIME_HOURS: Final = "h"
TIME_DAYS: Final = "d"
TIME_WEEKS: Final = "w"
TIME_MONTHS: Final = "m"
TIME_YEARS: Final = "y"

# Length units
LENGTH_MILLIMETERS: Final = "mm"
LENGTH_CENTIMETERS: Final = "cm"
LENGTH_METERS: Final = "m"
LENGTH_KILOMETERS: Final = "km"

LENGTH_INCHES: Final = "in"
LENGTH_FEET: Final = "ft"
LENGTH_YARD: Final = "yd"
LENGTH_MILES: Final = "mi"

# Frequency units
FREQUENCY_HERTZ: Final = "Hz"
FREQUENCY_KILOHERTZ: Final = "kHz"
FREQUENCY_MEGAHERTZ: Final = "MHz"
FREQUENCY_GIGAHERTZ: Final = "GHz"

# Pressure units
PRESSURE_PA: Final = "Pa"
PRESSURE_HPA: Final = "hPa"
PRESSURE_KPA: Final = "kPa"
PRESSURE_BAR: Final = "bar"
PRESSURE_CBAR: Final = "cbar"
PRESSURE_MBAR: Final = "mbar"
PRESSURE_MMHG: Final = "mmHg"
PRESSURE_INHG: Final = "inHg"
PRESSURE_PSI: Final = "psi"

# Sound pressure units
SOUND_PRESSURE_DB: Final = "dB"
SOUND_PRESSURE_WEIGHTED_DBA: Final = "dBa"

# Volume units
VOLUME_LITERS: Final = "L"
VOLUME_MILLILITERS: Final = "mL"
VOLUME_CUBIC_METERS: Final = "m³"
VOLUME_CUBIC_FEET: Final = "ft³"

VOLUME_GALLONS: Final = "gal"
VOLUME_FLUID_OUNCE: Final = "fl. oz."

# Volume Flow Rate units
VOLUME_FLOW_RATE_CUBIC_METERS_PER_HOUR: Final = "m³/h"
VOLUME_FLOW_RATE_CUBIC_FEET_PER_MINUTE: Final = "ft³/m"

# Area units
AREA_SQUARE_METERS: Final = "m²"

# Mass units
MASS_GRAMS: Final = "g"
MASS_KILOGRAMS: Final = "kg"
MASS_MILLIGRAMS: Final = "mg"
MASS_MICROGRAMS: Final = "µg"

MASS_OUNCES: Final = "oz"
MASS_POUNDS: Final = "lb"

# Conductivity units
CONDUCTIVITY: Final = "µS/cm"

# Light units
LIGHT_LUX: Final = "lx"

# UV Index units
UV_INDEX: Final = "UV index"

# Percentage units
PERCENTAGE: Final = "%"

# Irradiation units
IRRADIATION_WATTS_PER_SQUARE_METER: Final = "W/m²"
IRRADIATION_BTUS_PER_HOUR_SQUARE_FOOT: Final = "BTU/(h×ft²)"

# Precipitation units
PRECIPITATION_MILLIMETERS_PER_HOUR: Final = "mm/h"
PRECIPITATION_INCHES: Final = "in"
PRECIPITATION_INCHES_PER_HOUR: Final = "in/h"

# Concentration units
CONCENTRATION_MICROGRAMS_PER_CUBIC_METER: Final = "µg/m³"
CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER: Final = "mg/m³"
CONCENTRATION_MICROGRAMS_PER_CUBIC_FOOT: Final = "μg/ft³"
CONCENTRATION_PARTS_PER_CUBIC_METER: Final = "p/m³"
CONCENTRATION_PARTS_PER_MILLION: Final = "ppm"
CONCENTRATION_PARTS_PER_BILLION: Final = "ppb"

# Speed units
SPEED_MILLIMETERS_PER_DAY: Final = "mm/d"
SPEED_FEET_PER_SECOND: Final = "ft/s"
SPEED_INCHES_PER_DAY: Final = "in/d"
SPEED_METERS_PER_SECOND: Final = "m/s"
SPEED_INCHES_PER_HOUR: Final = "in/h"
SPEED_KILOMETERS_PER_HOUR: Final = "km/h"
SPEED_KNOTS: Final = "kn"
SPEED_MILES_PER_HOUR: Final = "mph"

# Signal_strength units
SIGNAL_STRENGTH_DECIBELS: Final = "dB"
SIGNAL_STRENGTH_DECIBELS_MILLIWATT: Final = "dBm"

# Data units
DATA_BITS: Final = "bit"
DATA_KILOBITS: Final = "kbit"
DATA_MEGABITS: Final = "Mbit"
DATA_GIGABITS: Final = "Gbit"
DATA_BYTES: Final = "B"
DATA_KILOBYTES: Final = "kB"
DATA_MEGABYTES: Final = "MB"
DATA_GIGABYTES: Final = "GB"
DATA_TERABYTES: Final = "TB"
DATA_PETABYTES: Final = "PB"
DATA_EXABYTES: Final = "EB"
DATA_ZETTABYTES: Final = "ZB"
DATA_YOTTABYTES: Final = "YB"
DATA_KIBIBYTES: Final = "KiB"
DATA_MEBIBYTES: Final = "MiB"
DATA_GIBIBYTES: Final = "GiB"
DATA_TEBIBYTES: Final = "TiB"
DATA_PEBIBYTES: Final = "PiB"
DATA_EXBIBYTES: Final = "EiB"
DATA_ZEBIBYTES: Final = "ZiB"
DATA_YOBIBYTES: Final = "YiB"

# Data_rate units
DATA_RATE_BITS_PER_SECOND: Final = "bit/s"
DATA_RATE_KILOBITS_PER_SECOND: Final = "kbit/s"
DATA_RATE_MEGABITS_PER_SECOND: Final = "Mbit/s"
DATA_RATE_GIGABITS_PER_SECOND: Final = "Gbit/s"
DATA_RATE_BYTES_PER_SECOND: Final = "B/s"
DATA_RATE_KILOBYTES_PER_SECOND: Final = "kB/s"
DATA_RATE_MEGABYTES_PER_SECOND: Final = "MB/s"
DATA_RATE_GIGABYTES_PER_SECOND: Final = "GB/s"
DATA_RATE_KIBIBYTES_PER_SECOND: Final = "KiB/s"
DATA_RATE_MEBIBYTES_PER_SECOND: Final = "MiB/s"
DATA_RATE_GIBIBYTES_PER_SECOND: Final = "GiB/s"
