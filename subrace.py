import requests
import utils
import create_char_shared as shared

def subrace(character):
    char = character
    char["state"] = "subrace"
    raceIndex = char["raceindex"]
    raceUrl = "http://dnd5eapi.co/api/races/" + str(raceIndex)
    r = requests.get(raceUrl)
    race = r.json()
    subraces = race["subraces"]
    subraceList = []
    if len(subraces) > 0:
        for subrace in subraces:
            subraceList.append(str(subrace["name"]))
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
    char["state"] = "subraceauto"
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
            a["score"] = a["score"] + abilityBoneses[currentAbilities.index(a)]
        char["abilities"] = currentAbilities
        profs = subrace["starting_proficiencies"]
        charProfs = char["proficiencies"]
        for p in profs:
            if str(p["name"]) not in charProfs:
                charProfs.append(str(p["name"]))
        traits = subrace["racial_traits"]
        charTraits = char["traits"]
        for t in traits:
            if str(t["name"]) not in charTraits:
                charTraits.append(str(t["name"]))
        langs = subrace["languages"]
        charLangs = char["languages"]
        for l in langs:
            if str(l["name"]) not in charLangs:
                charLangs.append(str(l["name"]))
        return char, None   
    else:
        return char, None

def setSubraceManual(character):
    print("set subrace manual")
    char = character
    char["state"] = "subracemanual"
    if char["subrace"] != None:
        url = "http://dnd5eapi.co/api/races/" + str(char["raceindex"])
        r = requests.get(url)
        subrace = r.json()
        if str(rjson["name"]) != str(char["race"]):
            print("Api race {} does not match choosen race {}. Saving and quitting").format(str(rjson["name"]), str(char["race"]) )
            return char, False
        else:
            value = ""
        char["manualState"] = "language"
        lastState = ""
        try:
            while value != "saveandquit" and value != "quit" and value != True:
                print("NOTHER STEP")
                if char["manualState"] == "language":
                    if "language_options" in subrace.keys():
                        char, value = shared.chooseLanguages(char, subrace)
                    lastState = "language"
                    char["manualState"] = "proficiency"
                elif char["manualState"] == "proficiency":
                    if "starting_proficiency_options" in subrace.keys():
                        char, value = shared.chooseProficiencies(char, subrace)
                    lastState = "proficiency"
                    char["manualState"] = "traits"
                elif char["manualState"] == "traits":
                    if "racial_trait_options" in subrace.keys():
                        char, value = shared.chooseTraits(char, subrace)
                    lastState = "traits"
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


