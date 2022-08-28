# Supported device classes

from .sensor.device_class import SensorDeviceClass  # backwards compatibility
from .sensor.device_class import SensorDeviceClass as DeviceClass

__all__ = ["DeviceClass", "SensorDeviceClass"]
