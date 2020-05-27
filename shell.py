# Hunter Harris & Austin Shah
# May 27 2020
# Basis Python Shell

# DEV THOUGTS
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

# =====================================================================
# Main Method
# =====================================================================

def main():

	startup()
	try:
		use()
	except KeyboardInterrupt:
		pass

	print("\nExiting turtle... goodbye :)")

# =====================================================================
# Helper Methods
# =====================================================================

def startup():
	rc = "assets/.turtlerc"
	if os.path.isfile(rc):
		subprocess.run("./{}".format(rc))
	else:
		print("no rc file found")

def use():
	cwd = os.getcwd()

	while True:
		command = input("\n{} -> ".format(cwd))
		opt = parseInput(command)
	
		# exit
		if opt == -1:
			break

		# execute command
		elif opt == 0:
			execute(command)

def execute(command):
	try:
		subprocess.run(command.split())
	except:
		print("ERROR Command not found : {}".format(command));

def parseInput(command):
	rawin = command.lower()
	if rawin == "exit" or rawin == "e":
		return -1
	elif rawin == "help":
		print("INSERT HELP MESSAGE HERE\n")
	else:
		return 0



if __name__ == "__main__":
	main()
