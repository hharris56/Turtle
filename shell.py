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

# =====================================================================
# Main Method
# =====================================================================

def main():

	startup()
	try:
		use()
	except KeyboardInterrupt:
		pass

	print("\nExiting TURTLE... goodbye :)")

# =====================================================================
# Helper Methods
# =====================================================================

# processes to be completed upon shell launch
def startup():
	rc = "assets/.turtlerc"
	if os.path.isfile(rc):
		subprocess.run("./{}".format(rc))
	else:
		print("no rc file found")

# main shell loop
# gets user input, passes to parseInput and possibly execute
def use():
	#cwd = os.getcwd()
	while True:
		#command = input("\n{} -> ".format(cwd))
		command = input("\nprompt -> ")
		opt = parseInput(command)
		# exit
		if opt == -1:
			break
		# execute command
		elif opt == 0:
			execute(command)

# executes the given command using subprocess.run
def execute(command):
	try:
		subprocess.run(command.split())
	except:
		print("ERROR Command not found : {}".format(command));

# parses user input
# return -1 to exit
# return 0 to execute
def parseInput(command):
	# check for key phrases
	rawin = command.lower()
	if rawin == "exit" or rawin == "e":
		return -1
	elif rawin == "help":
		print("INSERT HELP MESSAGE HERE\n")
	else:
		return 0



if __name__ == "__main__":
	main()
