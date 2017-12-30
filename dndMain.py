import sys
import random
import os

def diceRoller():
	goodSelection = False
	selection = ""
	while goodSelection == False:
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
		selection = input("ENTER NUMERIC COMMAND:  ")
		try:
			command = int(selection)
			if command == 1:
				print("roll20")
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
				print("done rollin")

		except:
			goodSelection = False

def roll(die):
	done = False
	rolls = []
	while done == False:
		num = random.randint(1,die)
		rolls.append(num)
		response = "ROLLED: "
		total = 0
		for number in rolls:
			response += str(number) + " "
			total += number
		if len(rolls) > 1:
			try:
			    response += " - TOTAL: " + str(total)
			except Exception, e:
				print("bad response")
				print(str(e))
		properAnswer = False
		again = ""
		properAnswers = ["y", "n", "yes", "no"]
		try:
		    again = raw_input("ROLL AGAIN? Y/N : ")
		except Exception, e:
			print("something didnt work")
			print(str(e))
		if again.lower() in ["n", "no"]:
			done = True

def rollSome(die, num, mod=0):
	rolls = []
	result = "ROLLED: "
	total = 0
	for x in range(0, num):
		roll = random.randint(1,die) + mod
		rolls.append(roll)
	for number in rolls:
		result += str(number) + " "
		total += number
	result += " - TOTAL: " + str(total)
	print(result)

def loadCharacterSelect():
	print(os.path.isfile("characterList.csv"))
	if os.path.isfile("characterList.csv"):
		file = open("characterList.csv", "r")
	else:
		file = open("characterList.csv", "w+")
	charArray = file.readlines()
	characters = []
	for char in charArray:
		if char.rstrip("\n") != "":
			characters.append(char.rstrip("\n"))
	return characters

def characterSelectMenu(characterArray):
	if characterArray != []:
		characterNumber = 0
		print("+++++++++++++++++++++++++++++++")
		print("-------CHARACTER SELECT--------")
		print("+++++++++++++++++++++++++++++++")
		for c in characterArray:
			characterNumber += 1
			print(str(characterNumber) + ": " + c)
		print("+++++++++++++++++++++++++++++++")
		goodSelect = False
		selection = ""
		while goodSelect == False:
			numberSelection = input("CHOOSE A CHARACTER: ")
			try:
				sn = int(numberSelection)
				selection = characterArray[sn-1]
				goodSelect = True
			except Exception as e:
				print("USE NUMERIC VALUE THAT IS SHOWN")
		return selection
	else:
		print("CURRENTLY NO CHARACTERS. \nYOU CAN CREATE CHARACTERS FROM THE MAIN MENU")
		return None


def playWithCharacter():
	characters = loadCharacterSelect()
	print(characters)
	characterName = characterSelectMenu(characters)
	if characterName != None:
		print(characterName)
	else:
		print("RETURNING TO MAIN MENU")



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
				print("creating character")
			elif command == 2:
				playWithCharacter()
			elif command == 3:
				print("edit character")
			elif command == 4:
				diceRoller()
			elif command == 5:
				print("exiting")
				goodSelection = True

		except:
			goodSelection = False

if __name__ == '__main__':
	main()