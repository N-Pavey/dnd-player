import requests
import utils

def subrace(character):
    char = character
    raceIndex = char["raceindex"]
    raceUrl = "http://dnd5eapi.co/api/races/" + raceIndex
    race = requests.get(raceUrl)
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

def setSubraceMnual(character):

