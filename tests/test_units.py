"""Tests for the Units enum string values (Home Assistant interop contract)."""

from sensor_state_data import Units

MICRO_SIGN = "µ"  # µ — the codepoint Home Assistant uses
GREEK_MU = "μ"  # μ — must never appear in a unit value


def test_micro_units_use_micro_sign() -> None:
    """Every "micro" unit must use U+00B5, matching Home Assistant.

    A Greek small letter mu (U+03BC) looks identical but compares unequal,
    silently breaking string equality against HA's constants. See issue #143.
    """
    micro_members = [u for u in Units if MICRO_SIGN in u.value or GREEK_MU in u.value]
    assert micro_members  # guard against the filter silently matching nothing
    for unit in micro_members:
        assert GREEK_MU not in unit.value, f"{unit.name} uses Greek mu U+03BC"
        assert MICRO_SIGN in unit.value


def test_specific_micro_unit_values() -> None:
    """Pin the previously-mismatched members to their HA string values."""
    assert Units.TIME_MICROSECONDS == MICRO_SIGN + "s"
    assert Units.CONCENTRATION_MICROGRAMS_PER_CUBIC_FOOT == MICRO_SIGN + "g/ft³"
