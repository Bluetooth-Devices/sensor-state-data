from sensor_state_data import Units


def test_unit_strings_match_home_assistant():
    """Pin unit strings to Home Assistant's homeassistant/const.py values."""
    assert Units("dBA") is Units.SOUND_PRESSURE_WEIGHTED_DBA
    assert Units("ft³/min") is Units.VOLUME_FLOW_RATE_CUBIC_FEET_PER_MINUTE
    # U+22C5 dot operator, not U+00D7 multiplication sign
    assert Units("BTU/(h⋅ft²)") is Units.IRRADIATION_BTUS_PER_HOUR_SQUARE_FOOT
