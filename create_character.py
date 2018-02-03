#import utils





def name(character):
    print("character")
    return character

def race(character):
    print("character")
    return character

def addClass(character):
    print("add class")
    return character

def abilities(character):
    print("abilities")
    return character

def equipment(character):
    print("equipment")
    return character



states = ["name", "race" "class", "abilities", "equipment"]
    
stages = {
    "name": name,
    "race": race,
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
        character["state"] = s
        value = stages.get(s)(character)
        if value == "saveandquit":
            return
        if value == "quit":
            return
        else:
            character = value




        
        
    

