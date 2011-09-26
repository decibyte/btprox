#!/usr/bin/python
# -*- coding: utf-8 -*-

# This plugin requires pysqueezecenter. Get it from: http://code.google.com/p/pysqueezecenter/
from pysqueezecenter.server import Server
from pysqueezecenter.player import Player

# Toggles Last.fm scrobbling depending on the presence of a device.
class ScrobbleToggler:

	# Example options:
	# 	{
	#		'server' : '1.2.3.4', # Server IP.
	# 	}

	def __init__(self, options):
		self.options = options

		self.server = Server(options['server'])
		self.server.connect()
		for p in self.server.get_players():
			p.display('Taking control!', 'btprox may now toggle scrobbling')
	
	# Set whether to scrobble or not
	def set_scrobbling(self, enable):
		scrobble = 1 if enable else 0
		self.server.request('pref plugin.audioscrobbler:enable_scrobbling %d' % scrobble)
		self.server.request('pref plugin.audioscrobbler:include_radio %s' % scrobble)
		for p in self.server.get_players():
			p.display('Scrobbling toggled by btprox', 'Scrobbling %s by btprox' % ('enabled' if enable else 'disabled'))

	def in_range(self, id, name):
		self.set_scrobbling(True)

	def out_of_range(self, id, name):
		self.set_scrobbling(False)
