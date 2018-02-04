import utils
import requests

abilitiyScores = ("strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma")
alignments = ("Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "Neutral", "Chaotic neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil")



def name(character):
    char = character
    char["state"] = "name"
    value = utils.enterText("ENTER YOUR CHARACTER'S NAME")
    char["name"] = value
    return char, value

def race(character):
    print("race")
    char = character
    char["state"] = "race"
    races = []
    r =  requests.get("http://dnd5eapi.co/api/races")
    rjson = r.json()
    for item in rjson["results"]:
        races.append(item["name"])
    race, index = utils.choiceMenu(races, "CHOOSE YOUR RACE")
    print(race)
    if race in races:
        char["race"] = race
        char["raceindex"] = index
        print(char)
        char, success = setRaceAuto(char)
        print("this is your character after auto bruh")
        print(char)
        if success != True:
            print("failed race auto set. Saving and quitting")
            return char, "saveandquit"
        else:
            char, success = setRaceManual(char)
            if success == True:
                print("success is true")
                return char, success
            else:
                print("success is not true")
                return char, success
    else:
        return char, race

def setRaceManual(character):
    print("setRaceManual")
    char = character
    print(char)
    char["state"] = "setRaceManual"
    url = "http://dnd5eapi.co/api/races/" + str(char["raceindex"])
    r = requests.get(url)
    rjson = r.json()
    if str(rjson["name"]) != str(char["race"]):
        print("Api race {} does not match choosen race {}. Saving and quitting").format(str(rjson["name"]), str(char["race"]) )
        return char, False
    else:
        value = ""
        char["manualState"] = "begin"
        lastState = ""
        try:
            while value != "saveandquit" and value != "quit" and value != True:
                print("NOTHER STEP")
                if char["manualState"] == "begin":
                    char["age"], value = utils.enterText("ENTER YOUR AGE")
                    lastState = "begin"
                    char["manualState"] = "language"
                elif char["manualState"] == "language":
                    if "language_options" in rjson.keys():
                        char, value = chooseLanguages(char, rjson)
                    lastState = "language"
                    char["manualState"] = "alignment"
                elif char["manualState"] == "alignment":
                    char["alignment"], value = utils.choiceMenu(alignments, "ENTER YOUR ALIGNMENT")
                    lastState = "alignment"
                    char["manualState"] = "proficiency"
                elif char["manualState"] == "proficiency":
                    if "starting_proficiency_options" in rjson.keys():
                        char, value = chooseProficiencies(char, rjson)
                    lastState = "proficiency"
                    char["manualState"] = "finish"
                elif char["manualState"] == "finish":
                    print("we did it!")
                    lastState = "finish"
                    value = True
            print("out of loop")
            char["manualState"] = lastState
            return char, value
        except Exception as e:
            print(e)



        char["manualState"] = lastState

def chooseProficiencies(character, rjson):
    print("Starting choose proficiencies")
    char = character
    pjson = rjson["starting_proficiency_options"]["from"]
    profs = []
    for p in pjson:
        profs.append(str(p["name"]))
    choose = int(rjson["starting_proficiency_options"]["choose"])
    char, value = utils.chooseMultiStepChar(char, "proficiencies", profs, choose, "SELECT PROFICIENCIES")
    return char, value


def chooseLanguages(character, rjson):
    print("starting choose languages")
    char = character
    ljson = rjson["language_options"]["from"]
    if str(ljson[0]["name"]) == "Any":
        l = requests.get("http://www.dnd5eapi.co/api/languages")
        lj = l.json()
        ljson = lj["results"]
    languages = []
    for lang in ljson:
        languages.append(str(lang["name"]))
    choose = int(rjson["language_options"]["choose"])
    char, value = utils.chooseMultiStepChar(char, "languages", languages, choose, "CHOOSE LANGUAGES")
    return char, value

                
        



def setRaceAuto(character):
    print("setRaceAuto")
    char = character
    char["state"] = "setRaceAuto"
    print("YOU CHOOSE: " + str(char["race"]).upper())
    url = "http://dnd5eapi.co/api/races/" + str(char["raceindex"])
    r = requests.get(url)
    rjson = r.json()
    if str(rjson["name"]) != str(char["race"]):
        print("Api race {} does not match choosen race {}. Saving and quitting").format(str(rjson["name"]), str(char["race"]) )
        return char, False
    else:
        char["abilities"] = {}
        for i in range (0, len(abilitiyScores)):
            char["abilities"][abilitiyScores[i]] = rjson["ability_bonuses"][i]
        char["size"] = str(rjson["size"])
        char["speed"] = str(rjson["speed"])
        char["proficiencies"] = []
        for p in rjson["starting_proficiencies"]:
            char["proficiencies"].append(str(p["name"]))
        char["languages"] = []
        for p in rjson["languages"]:
            char["languages"].append(str(p["name"]))
        char["traits"] = []
        for p in rjson["traits"]:
            char["traits"].append(str(p["name"]))
        print(char)
        return char, True



        
            





def addClass(character):
    print("add class")
    return character, None

def abilities(character):
    print("abilities")
    return character, None

def equipment(character):
    print("equipment")
    return character, None



states = ("name", "race", "setRaceAuto", "setRaceManual", "class", "abilities", "equipment")
    
stages = {
    "name": name,
    "race": race,
    "setRaceAuto": setRaceAuto,
    "setRaceManual": setRaceManual,
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




        
        
    

