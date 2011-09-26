#!/usr/bin/python
# -*- coding: utf-8 -*-

import bluetooth
import config

# Dictionary of devices in range and their names
devices_in_range = {}

# Dictionary of devices that seem to be away (for how many scans), but should not be regarded as
# out of sight yet.
devices_not_seen = {}

# Scan for devices and update the list of devices and names.
def scan():
	# Get devices in range.
	devices = bluetooth.discover_devices()

	# Loop through devices in range.
	for d in devices:
		if not d in devices_in_range.keys():
			devices_in_range[d] = bluetooth.lookup_name(d)
			if d in config.known_devices.values():
				print 'known device %s (%s) in range' % (d, devices_in_range[d],)
			else:
				print '%s (%s) in range' % (d, devices_in_range[d],)
		else:
			print '%s still in range' % d

	# Loop through devices known to be in range and remove those that should be regarded as not in range.
	to_remove = []
	for d in devices_in_range:
		if not d in devices:
			# Update device away scan count.
			if devices_not_seen.has_key(d):
				devices_not_seen[d] += 1
			else:
				devices_not_seen[d] = 1
			# Remove device if away scan count is too high now.
			if devices_not_seen[d] >= config.away_after:
				to_remove.append(d)
				if d in config.known_devices.values():
					print 'known device %s (%s) no longer in range' % (d, devices_in_range[d],)
				else:
					print '%s (%s) no longer in range' % (d, devices_in_range[d],)
			else:
				print '%s seems to be away, missing for %i of %i scans.' % (d, devices_not_seen[d], config.away_after,)
		# Device IS in range. Reset the away scan counter.
		else:
			if devices_not_seen.has_key(d):
				del devices_not_seen[d]
	for d in to_remove:
		del devices_not_seen[d]
		del devices_in_range[d]

# Start the loop
while True:
	print '*' * 72
	scan()
