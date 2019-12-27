#!/usr/bin/env python3

import gi
import alsaaudio
import time
import os
import sys
import psutil
import logging
import subprocess
from pynput.keyboard import Key, Controller, KeyCode

gi.require_version("Wnck", "3.0")
from gi.repository import Wnck

keyboard = Controller()
adsnames = ['Advertisement','Spotify']

def search():
	scr = Wnck.Screen.get_default()
	scr.force_update()
	windows = scr.get_windows()
	for window in windows:
		if window.get_icon_name() in adsnames:
			print(window.get_icon_name() + " ad detected, rebooting spotify")
			p = psutil.Process(window.get_pid())
			p.kill()
			subprocess.Popen(["nohup", "spotify", "&>", "/dev/null", "2>&1&"], shell=False, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
			time.sleep(4)
			"""Press play/pause button to launch music """
			print("play music")
			keyboard.press(KeyCode.from_vk(269025044))
			keyboard.release(KeyCode.from_vk(269025044))
	time.sleep(1)

def restart_program():
	"""Restarts the current program, with file objects and descriptors cleanup"""
	p = psutil.Process(os.getpid())
	for handler in p.open_files() + p.connections():
		os.close(handler.fd)
	python = sys.executable
	os.execl(python, python, *sys.argv)

search()
restart_program()
