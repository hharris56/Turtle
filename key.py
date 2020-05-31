# Hunter Harris & Austin Shah
# May 27 2020
# Basis Python Shell

# DEV COMMENTS
"""
cd is not a 'command', must impliment a way to change current
working directory
	- will need os

"""
 
# =====================================================================
# Imports and Global Constants
# =====================================================================

import os
import subprocess
from pynput.keyboard import Controller, Key, Listener
from pynput import keyboard
import time
import string

controller = Controller()
current_command = ""

# =====================================================================
# Main Method
# =====================================================================

def main():
	with Listener(on_press=on_press, on_release=on_release) as listener:
		listener.join()

# =====================================================================
# Helper Methods
# =====================================================================

def on_press(key):
	#print("{0} pressed".format(key))
	try:
		key.char
	except AttributeError:
		print("special key")

def on_release(key):
	print("{0} release".format(key))
	if key == keyboard.Key.esc:
		return False

if __name__ == "__main__":
	main()
