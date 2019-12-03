#!/usr/bin/env python3

import gi
import alsaaudio
import time
import os
import sys
import psutil
import logging

gi.require_version("Wnck", "3.0")
from gi.repository import Wnck

adsnames = ['Advertisement','Spotify']
m = alsaaudio.Mixer()

def search(m):
	pubdetected = False
	scr = Wnck.Screen.get_default()
	scr.force_update()
	windows = scr.get_windows()
	for window in windows:
		if window.get_icon_name() in adsnames:
			print(window.get_icon_name() + " => Ad detected, muted")
			pubdetected = True
	if pubdetected:
		m.setvolume(0)
	else:
		m.setvolume(80)
	time.sleep(1)

def restart_program():
	"""Restarts the current program, with file objects and descriptors cleanup"""
	try:
		p = psutil.Process(os.getpid())
		for handler in p.open_files() + p.connections():
			os.close(handler.fd)
	except Exception as e:
		logging.error(e)

	python = sys.executable
	os.execl(python, python, *sys.argv)

search(m)
restart_program()
