import requests
import utils

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