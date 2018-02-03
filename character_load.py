import os


def loadCharacterSelect():
	print(os.path.isfile("characters/characterList.csv"))
	if os.path.isfile("characters/characterList.csv"):
		file = open("characters/characterList.csv", "r")
	else:
		file = open("characters/characterList.csv", "w+")
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
        exitNumber = characterNumber+1
        print(str(characterNumber+1) + ": GO BACK")
        print("+++++++++++++++++++++++++++++++")
        goodSelect = False
        selection = ""
        while goodSelect == False:
            numberSelection = input("CHOOSE A CHARACTER: ")
            try:
                sn = int(numberSelection)
                if sn == exitNumber:
                    goodselect = True
                    return None
                else:
                    selection = characterArray[sn-1]
                    goodSelect = True
            except Exception as e:
                print("USE NUMERIC VALUE THAT IS SHOWN")
            return selection
    else:
        print("CURRENTLY NO CHARACTERS. \nYOU CAN CREATE CHARACTERS FROM THE MAIN MENU")
        return None