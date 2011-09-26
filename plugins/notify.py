#!/usr/bin/python
# -*- coding: utf-8 -*-

import pynotify, sys

if not pynotify.init('icon-summary'):
	sys.exit(1)

class Notifier:
	def __init__(self, options):
		self.options = options
	
	# Make an onscreen notification
	def notify(self, title, in_range):
		n = pynotify.Notification(title, '', 'file:///usr/share/icons/ubuntu-mono-dark/status/24/bluetooth-active.svg' if in_range else 'file:///usr/share/icons/ubuntu-mono-dark/status/24/bluetooth-disabled.svg')
		n.show()

	def in_range(self, id, name):
		self.notify('%s (%s) in range' % (name, id,), True)
	
	def out_of_range(self, id, name):
		self.notify('%s (%s) out of range' % (name, id,), False)
