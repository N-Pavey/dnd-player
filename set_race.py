import utils
import requests
import create_char_shared as shared



abilitiyScores = ("strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma")
alignments = ("Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "Neutral", "Chaotic neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil")


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
        return char, race
    else:
        return char, race


def setRaceManual(character):
    print("setRaceManual")
    char = character
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
                        char, value = shared.chooseLanguages(char, rjson)
                    lastState = "language"
                    char["manualState"] = "alignment"
                elif char["manualState"] == "alignment":
                    char["alignment"], value = utils.choiceMenu(alignments, "ENTER YOUR ALIGNMENT")
                    lastState = "alignment"
                    char["manualState"] = "proficiency"
                elif char["manualState"] == "proficiency":
                    if "starting_proficiency_options" in rjson.keys():
                        char, value = shared.chooseProficiencies(char, rjson)
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