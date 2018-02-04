def choiceMenu(choices, message):
    goodselection = False
    while goodselection == False:
        choiceNumber = 0
        print("+++++++++++++++++++++++++++++++")
        print(message)
        for c in choices:
            choiceNumber+=1
            print(str(choiceNumber) + ": " + c)
        snq = choiceNumber + 1
        q = choiceNumber + 2
        print(str(snq) + ": SAVE AND QUIT")
        print(str(q) + ": QUIT")
        try:
            selection = input("ENTER A NUMERIC VALUE: ")
            sn = int(selection)
            if sn == snq:
                return "saveandquit", "saveandquit"
            if sn == q:
                return "quit", "quit"
            choice = str(choices[sn-1])
            goodselection = True
        except:
            print("PLEASE SELECT A SHOWN NUMERIC VALUE")
    return choice, sn

def enterText(message):
    goodInput = False
    while goodInput == False:
        print("+++++++++++++++++++++++++++++++")
        print(message + ": ")
        print("1: SAVE AND QUIT")
        print("2: QUIT")
        userInput = raw_input("ENTER CHOICE: ")
        if userInput.strip() == "1":
            return  "saveandquit"
        if userInput.strip() == "2":
            return "quit"
        if userInput.strip() == "":
            print("PLEASE ENTER A VALUE")
        else:
            print("good age")
            goodInput = True
    return userInput.strip()

def chooseMultiStepChar(character, attribute, choices, rounds, message):
    char = character
    i = 0
    value = ""
    while i<rounds and value != "quit" and value != "saveandquit":
        selection, value = choiceMenu(choices, message + ": " + str(i+1) + "/" + str(rounds))
        char[attribute].append(selection)
    return char, value