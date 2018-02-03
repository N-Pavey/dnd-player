def choiceMenu(choices):
    goodselection = False
    while goodselection == False:
        choiceNumber = 0
        print("+++++++++++++++++++++++++++++++")
        for c in choices:
            choiceNumber+=1
            print(str(choiceNumber) + ": " + c)
        snq = choiceNumber + 1
        q = choiceNumber + 2
        print(str(snq) + ": SAVE AND QUIT")
        print(str(q) + ": QUIT")
        selection = input("ENTER A NUMERIC VALUE")
        try:
            sn = int(selection)
            if sn == snq:
                return "saveandquit"
            if sn == q:
                return "quit"
            choice = choices[sn-1]
            goodselection = True
        except:
            print("PLEASE SELECT A SHOWN NUMERIC VALUE")
    return choice
        
        
    

