# Changelog

<!--next-version-placeholder-->

## v2.3.0 (2022-08-17)
### Feature
* New base sensors ([#27](https://github.com/Bluetooth-Devices/sensor-state-data/issues/27)) ([`b7637bf`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/b7637bf725a12fdf0f358a52c94eda54b89303c6))

## v2.2.0 (2022-08-13)
### Feature
* Add set_precision convenience method ([#26](https://github.com/Bluetooth-Devices/sensor-state-data/issues/26)) ([`0937284`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/0937284a66bd9b2494817aa0402235cd1635d0f3))

## v2.1.2 (2022-08-11)
### Fix
* Export BinarySensorDescription ([#25](https://github.com/Bluetooth-Devices/sensor-state-data/issues/25)) ([`ecc7331`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/ecc73310db03f40b0e78d27a6ab0aa7f665f4f18))

## v2.1.1 (2022-08-11)
### Fix
* Add default factories for descriptions and values ([#24](https://github.com/Bluetooth-Devices/sensor-state-data/issues/24)) ([`519ac61`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/519ac61debf227ed36cd4855a3c77cc4c6db5432))

## v2.1.0 (2022-08-11)
### Feature
* Add support for binary sensors ([#23](https://github.com/Bluetooth-Devices/sensor-state-data/issues/23)) ([`902fb76`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/902fb7624d51627bd02e190f67d3234a17d4615a))

## v2.0.2 (2022-07-21)
### Fix
* Typing on native_unit_of_measurement ([#22](https://github.com/Bluetooth-Devices/sensor-state-data/issues/22)) ([`9815b3d`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/9815b3d679fb0f4416f4919c4246c45e7bed6806))

## v2.0.1 (2022-07-21)
### Fix
* Name and device type were not being set from refactor ([#21](https://github.com/Bluetooth-Devices/sensor-state-data/issues/21)) ([`2badc47`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/2badc471e96493437f7eea3bc8629894edd79217))

## v2.0.0 (2022-07-21)
### Feature
* Refactor to split name and units ([#20](https://github.com/Bluetooth-Devices/sensor-state-data/issues/20)) ([`e06c200`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/e06c20084ea106a2e9c6e506953c210bd90d0d10))

### Breaking
* Library has changed to have units ([`e06c200`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/e06c20084ea106a2e9c6e506953c210bd90d0d10))
* name is now moved to SensorValue ([`e06c200`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/e06c20084ea106a2e9c6e506953c210bd90d0d10))
* SensorDeviceInfo is now a dataclass ([`e06c200`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/e06c20084ea106a2e9c6e506953c210bd90d0d10))
* Units are now an str enum ([`e06c200`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/e06c20084ea106a2e9c6e506953c210bd90d0d10))

## v1.11.1 (2022-07-20)
### Fix
* Adjust naming to account for _s ([#19](https://github.com/Bluetooth-Devices/sensor-state-data/issues/19)) ([`ab600f5`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/ab600f51294510418b1502d72dfc84f88944c535))
* Do not prefix device name since hass will use entity_name ([#18](https://github.com/Bluetooth-Devices/sensor-state-data/issues/18)) ([`728be53`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/728be53bd3767b1f7c0a1f79ba37950cb7a13e2d))

## v1.11.0 (2022-07-19)
### Feature
* Rename _update_from_data to _start_update ([#17](https://github.com/Bluetooth-Devices/sensor-state-data/issues/17)) ([`3235362`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/3235362010113fd2a1903ede58fa39ce5854c38a))

## v1.10.0 (2022-07-19)
### Feature
* Export consts ([#16](https://github.com/Bluetooth-Devices/sensor-state-data/issues/16)) ([`177db6f`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/177db6f84519c2817bd891b8ad8ae2cb13414cd1))

## v1.9.0 (2022-07-19)
### Feature
* Allow setting the key for a predefined sensor ([#15](https://github.com/Bluetooth-Devices/sensor-state-data/issues/15)) ([`519b4e2`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/519b4e28d4d41f5ed24f326ae17507fc3321534a))

## v1.8.0 (2022-07-19)
### Feature
* Add the ability to set manufacturer/sw_version/hw_version ([#14](https://github.com/Bluetooth-Devices/sensor-state-data/issues/14)) ([`fef90fe`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/fef90fed29c1963ed00a75b9b6eaf78adcd34075))

## v1.7.0 (2022-07-19)
### Feature
* Add title property ([#13](https://github.com/Bluetooth-Devices/sensor-state-data/issues/13)) ([`7aa2690`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/7aa26901f77a8ad4109465c6232d8ae9ea99432c))

## v1.6.0 (2022-07-19)
### Feature
* Add primary_device_id property ([#12](https://github.com/Bluetooth-Devices/sensor-state-data/issues/12)) ([`6ee964b`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/6ee964b98b144a6f7c1e78444972e4759ee6223e))

## v1.5.1 (2022-07-19)
### Fix
* Fix __all__ ([#11](https://github.com/Bluetooth-Devices/sensor-state-data/issues/11)) ([`6f99e5f`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/6f99e5f6f3c3021ad320527e3024f5dbcb6186aa))

## v1.5.0 (2022-07-19)
### Feature
* Change model ([#10](https://github.com/Bluetooth-Devices/sensor-state-data/issues/10)) ([`a57ef64`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/a57ef64a255e6e40cdeea6332937a0f0891b1b3f))

## v1.4.1 (2022-07-19)
### Fix
* Sensor library should not be an enum ([#9](https://github.com/Bluetooth-Devices/sensor-state-data/issues/9)) ([`bed9997`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/bed9997e57f073e581c26329629ef0e05f8980c3))

## v1.4.0 (2022-07-19)
### Feature
* Update format ([#8](https://github.com/Bluetooth-Devices/sensor-state-data/issues/8)) ([`f8e4cdc`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/f8e4cdcacb415fd5c446e1ec263b19397c49b840))

## v1.3.1 (2022-07-18)
### Fix
* Refactor update_predefined_sensor ([#7](https://github.com/Bluetooth-Devices/sensor-state-data/issues/7)) ([`3e10e0e`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/3e10e0e20c274cb7f334ed8590d90d7fb10c622d))

## v1.3.0 (2022-07-18)
### Feature
* Add data ([#5](https://github.com/Bluetooth-Devices/sensor-state-data/issues/5)) ([`206f42d`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/206f42d5b14e80995e78ff5d658d3f0a3f0edc37))

### Fix
* Drop unused os ([#6](https://github.com/Bluetooth-Devices/sensor-state-data/issues/6)) ([`a5514fe`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/a5514fe2135659c026e8f629d96a2337bf49cfc1))

## v1.2.1 (2022-07-18)
### Fix
* Fix release process ([#4](https://github.com/Bluetooth-Devices/sensor-state-data/issues/4)) ([`fe660c3`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/fe660c3ea4a2b964f32e50801ddc4f4c8c85fdd4))

## v1.2.0 (2022-07-18)
### Feature
* Add library ([#3](https://github.com/Bluetooth-Devices/sensor-state-data/issues/3)) ([`c7d12fc`](https://github.com/Bluetooth-Devices/sensor-state-data/commit/c7d12fc63e9e253c3548951bd8c3c0dfc6620dde))
