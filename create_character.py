import utils
import requests

abilitiyScores = ("strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma")



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
    print race
    if race in races:
        char["race"] = race
        char["raceindex"] = index
        print(char)
        char, value = setRace(char) 
    else:
        return char, race

def setRace(character):
    print("setRace")
    char = character
    char["state"] = "setRace"
    print("YOU CHOOSE: " + str(char["race"]).upper())
    url = "http://dnd5eapi.co/api/races/" + str(char["raceindex"])
    r = requests.get(url)
    rjson = r.json()
    if str(rjson["name"]) != str(char["race"]):
        print("Api race does not match choosen race. Saving and quitting")
        return char, "saveandquit"
    else:
        char["abilities"] = {}
        for i in range (0, len(abilitiyScores)):
            char["abilities"][abilitiyScores[i]] = rjson["ability_bonuses"][i]
        char["size"] = str(rjson["size"])
        char["proficiencies"] = []
        for p in rjson["starting_proficiencies"]:
            char["proficiencies"].append(p["name"])

        
            





def addClass(character):
    print("add class")
    return character, None

def abilities(character):
    print("abilities")
    return character, None

def equipment(character):
    print("equipment")
    return character, None



states = ["name", "race", "setRace" "class", "abilities", "equipment"]
    
stages = {
    "name": name,
    "race": race,
    "setRace": setRace,
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




        
        
    

