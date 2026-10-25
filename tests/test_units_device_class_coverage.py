from sensor_state_data import Units


def test_reactive_energy_units():
    assert Units.ENERGY_VOLT_AMPERE_REACTIVE_HOUR.value == "varh"
    assert Units.ENERGY_KILO_VOLT_AMPERE_REACTIVE_HOUR.value == "kvarh"


def test_energy_distance_units():
    assert Units.ENERGY_DISTANCE_KILO_WATT_HOUR_PER_100_KM.value == "kWh/100km"
    assert Units.ENERGY_DISTANCE_WATT_HOUR_PER_KM.value == "Wh/km"
    assert Units.ENERGY_DISTANCE_MILES_PER_KILO_WATT_HOUR.value == "mi/kWh"
    assert Units.ENERGY_DISTANCE_KM_PER_KILO_WATT_HOUR.value == "km/kWh"


def test_blood_glucose_concentration_units():
    assert Units.BLOOD_GLUCOSE_MILLIGRAMS_PER_DECILITER.value == "mg/dL"
    assert Units.BLOOD_GLUCOSE_MILLIMOLE_PER_LITER.value == "mmol/L"


def test_radiation_concentration_units():
    assert Units.RADIATION_BECQUEREL_PER_CUBIC_METER.value == "Bq/m³"
    assert Units.RADIATION_PICOCURIES_PER_LITER.value == "pCi/L"


def test_new_units_are_distinct_members():
    """None of the new values may collide with an existing member (see #140)."""
    values = [
        "varh",
        "kvarh",
        "kWh/100km",
        "Wh/km",
        "mi/kWh",
        "km/kWh",
        "mg/dL",
        "mmol/L",
        "Bq/m³",
        "pCi/L",
    ]
    assert len({Units(value).name for value in values}) == len(values)
