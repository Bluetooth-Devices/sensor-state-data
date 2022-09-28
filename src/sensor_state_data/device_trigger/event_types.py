# Supported event types
from __future__ import annotations

from ..enum import StrEnum


class EventTypes(StrEnum):
    """Device trigger event types."""

    # Turn on
    TURN_ON = "turn_on"

    # Turn off
    TURN_OFF = "turn_off"

    # Toggle
    TOGGLE = "toggle"

    # Button press
    PRESS = "press"

    # Single press
    SINGLE_PRESS = "single_press"

    # Double press
    DOUBLE_PRESS = "double_press"

    # Triple press
    TRIPLE_PRESS = "triple_press"

    # long single press
    LONG_SINGLE_PRESS = "long_single_press"

    # long double press
    LONG_DOUBLE_PRESS = "long_double_press"

    # Long triple press
    LONG_TRIPLE_PRESS = "long_triple_press"

    # Rotate left
    ROTATE_LEFT = "rotate_left"

    # Rotate right
    ROTATE_RIGHT = "rotate_right"
