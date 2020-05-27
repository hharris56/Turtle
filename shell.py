# Hunter Harris & Austin Shah
# May 27 2020
# Basis Python Shell

# =====================================================================
# Imports and Global Constants
# =====================================================================

import subprocess

# =====================================================================
# Main Method
# =====================================================================

def main():
	while True:
		userin = input("-> ")
		if userin == "exit":
			break
		elif userin == "help":
			print("HELP MESSAGE")
		else:
			excecute(userin)

# =====================================================================
# Helper Methods
# =====================================================================

def excecute(command):
	# parse_input(userinput)	
	try:
		subprocess.run(command.split())
	except:
		print("ERROR Command not found : {}".format(command));

def parse_input(userin):
	pass




if __name__ == "__main__":
	main();
