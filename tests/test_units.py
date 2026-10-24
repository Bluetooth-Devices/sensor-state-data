"""Tests for the Units enum string values (Home Assistant interop contract)."""

import pytest

from sensor_state_data import Units

GREEK_MU = "μ"  # μ — the micro prefix Home Assistant uses since 2025.9
MICRO_SIGN = "µ"  # µ — legacy micro sign, must never appear in a unit value


def test_micro_units_use_greek_mu() -> None:
    """Every "micro" unit must use U+03BC, matching Home Assistant.

    The two codepoints look identical but compare unequal, silently
    breaking string equality against HA's constants. See issue #143.
    """
    micro_members = [u for u in Units if MICRO_SIGN in u.value or GREEK_MU in u.value]
    assert len(micro_members) == 5
    for unit in micro_members:
        assert MICRO_SIGN not in unit.value, f"{unit.name} uses micro sign U+00B5"


def test_specific_micro_unit_values() -> None:
    """Pin micro members to Home Assistant's string values."""
    assert Units.TIME_MICROSECONDS.value == GREEK_MU + "s"
    assert Units.MASS_MICROGRAMS.value == GREEK_MU + "g"
    assert Units.CONDUCTIVITY.value == GREEK_MU + "S/cm"
    assert Units.CONCENTRATION_MICROGRAMS_PER_CUBIC_METER.value == GREEK_MU + "g/m³"
    assert Units.CONCENTRATION_MICROGRAMS_PER_CUBIC_FOOT.value == GREEK_MU + "g/ft³"


@pytest.mark.parametrize("value", ["µs", "µg", "µS/cm", "µg/m³", "µg/ft³"])
def test_legacy_micro_sign_lookup(value: str) -> None:
    """Looking a unit up by the legacy micro sign still resolves."""
    assert MICRO_SIGN in value
    assert Units(value).value == value.replace(MICRO_SIGN, GREEK_MU)


def test_unknown_value_still_raises() -> None:
    with pytest.raises(ValueError):
        Units("µnope")
    with pytest.raises(ValueError):
        Units("nope")
