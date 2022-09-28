# Supported devices keys for devices that fire events

from ..enum import StrEnum


class EventDeviceKeys(StrEnum):
    """Keys for devices that send events."""

    # Rocker switch
    SWITCH = "switch"

    # Dimmer
    DIMMER = "dimmer"

    # Button
    BUTTON = "button"
