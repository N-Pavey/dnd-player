import sys
import random
import os
import dice
import character_load as loadChar
import create_character as create



def playWithCharacter():
	characters = loadChar.loadCharacterSelect()
	print(characters)
	characterName = loadChar.characterSelectMenu(characters)
	if characterName != None:
		print(characterName)
	else:
		print("RETURNING TO MAIN MENU")

def createCharacter():
	create.start()



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
	goodSelection = False
	selection = ""
	while goodSelection == False:
		print("+++++++++++++++++++++++++++++++")
		print("-----------MAIN MENU-----------")
		print("+++++++++++++++++++++++++++++++")
		print("1. CREATE CHARACTER (NOT DONE)")
		print("2. PLAY WITH EXISTING CHARACTER (NOT DONE)")
		print("3. EDIT CHARACTER (NOT DONE")
		print("4. SIMPLE DICE ROLLER (NOT DONE)")
		print("5. EXIT")
		print("+++++++++++++++++++++++++++++++")


		selection = input("ENTER NUMERIC COMMAND:  ")
		try:
			command = int(selection)
			if command == 1:
				createCharacter()
			elif command == 2:
				playWithCharacter()
			elif command == 3:
				print("edit character")
			elif command == 4:
				dice.diceRoller()
			elif command == 5:
				print("exiting")
				goodSelection = True

		except:
			goodSelection = False

if __name__ == '__main__':
	main()