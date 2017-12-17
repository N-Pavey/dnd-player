import sys
import random

def diceRoller():
	print("+++++++++++++++++++++++++++++++")
	print("----------DICE ROLLER----------")
	print("+++++++++++++++++++++++++++++++")
	print("1. ROLL 20")
	print("2. ROLL 12")
	print("3. ROLL 10")
	print("4. ROLL  8")
	print("5. ROLL  6")
	print("6. ROLL  4")
	print("7. FLIP COIN")
	print("8. EXIT")
	print("+++++++++++++++++++++++++++++++")
	goodSelection = False
	selection = ""
	while goodSelection == False:
	    selection = input("ENTER NUMERIC COMMAND:  ")
	    try:
	    	command = int(selection)
	    	if command == 1:
	    		die = 20
	    	elif command == 2:
	    		die = 12
	    	elif command == 3:
	    		die = 10
	    	elif command == 4:
	    		die = 8
	    	elif command == 5:
	    		die = 6
	    	elif command == 6:
	    		die = 4
	    	elif command == 7:
	    		die = 2
	    	elif command == 8:
	    		print("exiting")
	    		goodSelection = True

	    	if goodSelection == False:
	    		roll(die)

	    except:
	    	goodSelection = False

def roll(die):
	done = False
	rolls = []
	while done == False:
		num = random.randint(1,die)
		done == True

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
	print("5. EXIT")
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

if __name__ == '__main__':
	main()