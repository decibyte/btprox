#!/usr/bin/python
# -*- coding: utf-8 -*-

# This is an example of the btprox configuration file.


# away_after determines when a device is regarded as out of sight. When
# a device has not been seen for this amount of scans, it is removed
# from the list of devices in range. This is used to make sure a device
# really is away, and show some tolerance to temporary scanning errors.
away_after = 3

# known_devices is a dictionary with human readable device names as
# keys and Bluetooth device MAC addresses as keys. Used for making it
# easier to reference devices, without having to remember
# MAC addresses.
known_devices = {
	'phone'      : '12:34:56:78:90:AB',
	'laptop'     : 'CD:EF:01:23:45:67',
}

# plugins is the list of plugins to load.
plugins = []
