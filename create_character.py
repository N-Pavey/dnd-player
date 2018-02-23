import utils
import requests
import set_race as setRace
import subrace as setSubrace




def name(character):
    char = character
    char["state"] = "name"
    name, value = utils.enterText("ENTER YOUR CHARACTER'S NAME")
    char["name"] = name
    return char, value




def race(character):
    print("add race")
    char = character
    char, value = setRace.race(char)
    return char, value

def setRaceAuto(character):
    print("setRaceAuto")
    char = character
    char, value = setRace.setRaceAuto(char)
    return char, value

def setRaceManual(character):
    print("set race manual")
    char = character
    char, value = setRace.setRaceManual(char)
    return char, value

def setSubraceAuto(character):
    print("set Subrace Auto")
    char = character
    char, value = setSubrace.setSubraceAuto(char)
    return char, value

def setSubraceManual(character):
    print("set Subrace Auto")
    char = character
    char, value = setSubrace.setSubraceManual(char)
    return char, value

def subrace(character):
    print("subrace")
    char = character
    char, value = setSubrace.subrace(char)
    return char, value

def addClass(character):
    print("add class")
    return character, None

def abilities(character):
    print("abilities")
    return character, None

def equipment(character):
    print("equipment")
    return character, None



states = ("name", "race", "setRaceAuto", "setRaceManual", "subrace", "setSubraceAuto", "setSubraceManual" "class", "abilities", "equipment")
    
stages = {
    "name": name,
    "race": race,
    "setRaceAuto": setRaceAuto,
    "setRaceManual": setRaceManual,
    "subrace": subrace,
    "setSubraceAuto": setSubraceAuto,
    "setSubraceManual": setSubraceManual,
    "class": addClass,
    "abilities": abilities,
    "equipment": equipment
    }

def start():
    # Name
    # race
    # class
    # ability scores
    # equipment
    character = {}
    for s in states:
        try:
            character["state"] = s
            returnChar, value = stages.get(s)(character)
            print("FINISHED STAGE: " + s)
            if value == "saveandquit":
                return
            if value == "quit":
                return
            else:
                character = returnChar
        except Exception as e:
            print("EXCEPTION")
            print(e)
    print("created character")
    print(character)




        
        
    

