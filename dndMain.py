import sys

def main():
	print("+++++++++++++++++++++++++++++++")
	print("-----WELCOME TO DND PLAYER-----")
	print("+++++++++++++++++++++++++++++++")
	print("-------------------------------")
	print("+++++++++++++++++++++++++++++++")
	print("")
	mainMenu()
	return

def mainMenu():
	print("+++++++++++++++++++++++++++++++")
	print("-----------MAIN MENU-----------")
	print("+++++++++++++++++++++++++++++++")
	print("1. CREATE CHARACTER (NOT DONE)")
	print("2. PLAY WITH EXISTING CHARACTER (NOT DONE)")
	print("3. EDIT CHARACTER (NOT DONE")
	print("4. SIMPLE DICE ROLLER (NOT DONE)")
	print("5. EXIT (NOT DONE)")
	print("+++++++++++++++++++++++++++++++")
	goodSelection = False
	selection = ""
	while goodSelection == False:
	    selection = input("ENTER NUMERIC COMMAND:  ")
	    try:
	    	command = int(selection)
	    	if command == 1:
	    		print("creating character")
	    	elif command == 2:
	    		print("load character")
	    	elif command == 3:
	    		print("edit character")
	    	elif command == 4:
	    		print("dice roller")
	    	elif command == 5:
	    		print("exiting")
	    		goodSelection = True


	    except:

	    	goodSelection = False

# def exit():
# 	print("EXITING")
# 	sys.exit()

if __name__ == '__main__':
	main()