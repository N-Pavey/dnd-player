import requests
import utils

def subrace(character):
    char = character
    raceIndex = char["raceindex"]
    raceUrl = "http://dnd5eapi.co/api/races/" + raceIndex
    r = requests.get(raceUrl)
    race = r.json()
    subraces = race["subraces"]
    subraceList = []
    if len(subraces) > 0:
        for subrace in subraces:
            subraceList.append(subrace["name"])
        subraceChoice, value = utils.choiceMenu(subraceList, "Choose your subrace")
        if value != "quit" and value != "saveandquit":
            char["subrace"] = subraceChoice
            for subrace in subraces:
                if subrace["name"] == subraceChoice:
                    subraceUrl = subrace["url"]
                    urlStrings = subraceUrl.split("/")
                    char["subraceindex"] = urlStrings[len(urlStrings)-1]
        return char, value
    else:
        char["subrace"] = None
        return char, None
    

def setSubraceAuto(character):
    char = character
    if char["subrace"] != None:
        url = "http://dnd5eapi.co/api/subraces/" + char["subraceindex"]
        r = requests.get(url)
        subrace = r.json()
        if subrace["name"] != char["subrace"]:
            print("ERROR subrace {} does not match character subrace {}").format(subrace["name"], char["subrace"])
            return char, "saveandquit"
        currentAbilities = char["abilities"]
        abilityBoneses = subrace["ability_bonuses"]
        for a in currentAbilities:
            a = a + abilityBoneses[currentAbilities.index(a)]
            
        
    else:
        return char, None

def setSubraceMnual(character):

