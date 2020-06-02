# Hunter Harris & Austin Shah
# May 27 2020
# Basic Python Shell

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
import keyboard
#import thread
import time

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
	while True:
		cwd = os.getcwd()
		command = input("\n{} -> ".format(cwd))
		#command = input("\nprompt -> ")
		opt = parseInput(command)
		# exit
		if opt == -1:
			break
		# execute command
		elif opt == 0:
			execute_command(command)

# executes the given command using subprocess.run (OUTDATED)
def execute(command):
	try:
		subprocess.run(command.split())
	except:
		print("ERROR Command not found : {}".format(command));

# change directory
def turtle_cd(path):
	"""convert to absolute path and change directory"""
	try:
		os.chdir(os.path.abspath(path))
	except Exception:
		print("FAILED, pick another existing directory you schizophrenic dipshit".format(path))

# executes the given command with support for pipes
def execute_command(command):
	"""execute commands and handle piping"""
	try:
		if "|" in command:
			#save for restoring later on
			s_in, s_out = (0, 0)
			s_in = os.dup(0)
			s_out = os.dup(1)

			#first command takes commandut from stdin
			fdin = os.dup(s_in)

			cmdlist = command.split("|")
			#iterate over all the commands that are piped
			for cmd in cmdlist:
				#fdin will be stdin if it's the first iteratic
				#and the readable end of the pipe if not.
				os.dup2(fdin, 0)
				os.close(fdin)

				#restore stdout if this is the last command
				if cmd == cmdlist[-1]:
					fdout = os.dup(s_out)
				else:
					fdin, fdout = os.pipe()

				#redirect stdout to pipe
				os.dup2(fdout, 1)
				os.close(fdout)

				try:
					subprocess.run(cmd.strip().split())
				except Exception:
					print("turtle: command not found: {}".format(cmd.strip()))

			#restore stdout and stdin
			os.dup2(s_in, 0)
			os.dup2(s_out, 1)
			os.close(s_in)
			os.close(s_out)
		else:
			subprocess.run(command.split(" "))
	except Exception:
		print("turtle: command not found: {}".format(command))


# parses user input
# return -1 to exit
# return 0 to execute
# return 1 to do nothing
def parseInput(command):
	# check for key phrases
	rawin = command.lower()
	if rawin == "exit" or rawin == "e":
		return -1
	elif rawin == "help":
		print("INSERT HELP MESSAGE HERE\n")

	# split the command + look for cd
	clist = command.split()
	if clist[0] == "cd":
		turtle_cd(clist[1])
		return 1

	else:
		return 0



if __name__ == "__main__":
	main()
