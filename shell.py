# Hunter Harris & Austin Shah
# May 27 2020
# Basis Python Shell

def main():
	while True:
		userin = input("-> ")
		if userin == "exit":
			break
		elif userin == "help":
			print("HELP MESSAGE")
		else:
			excecute(userin)

def excecute(userinput):
	pass

if __name__ == "__main__":
	main();
