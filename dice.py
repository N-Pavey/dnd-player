import random

def diceRoller():
	exitSelection = False
	selection = ""
	while exitSelection == False:
		print "+++++++++++++++++++++++++++++++"
		print("----------DICE ROLLER----------")
		print("+++++++++++++++++++++++++++++++")
		print("1. ROLL 20")
		print("2. ROLL 12")
		print("3. ROLL 10")
		print("4. ROLL  8")
		print("5. ROLL  6")
		print("6. ROLL  4")
		print("7. FLIP COIN")
		print("8. EXIT")
		print("+++++++++++++++++++++++++++++++")
		selection = input("ENTER NUMERIC COMMAND:  ")
		try:
			command = int(selection)
			if command == 1:
				print("roll20")
				die = 20
			elif command == 2:
				die = 12
			elif command == 3:
				die = 10
			elif command == 4:
				die = 8
			elif command == 5:
				die = 6
			elif command == 6:
				die = 4
			elif command == 7:
				die = 2
			elif command == 8:
				print("exiting")
				goodSelection = True
			if exitSelection == False:
				roll(die)
				print("done rollin")

		except:
			exitSelection = False

def roll(die):
	done = False
	rolls = []
	while done == False:
		num = random.randint(1,die)
		rolls.append(num)
		response = "ROLLED: "
		total = 0
		for number in rolls:
			response += str(number) + " "
			total += number
		if len(rolls) > 1:
			try:
			    response += " - TOTAL: " + str(total)
			except Exception, e:
				print("bad response")
				print(str(e))
		properAnswer = False
		again = ""
		properAnswers = ["y", "n", "yes", "no"]
		try:
		    again = raw_input("ROLL AGAIN? Y/N : ")
		except Exception, e:
			print("something didnt work")
			print(str(e))
		if again.lower() in ["n", "no"]:
			done = True

def rollSome(die, num, mod=0):
	rolls = []
	result = "ROLLED: "
	total = 0
	for x in range(0, num):
		roll = random.randint(1,die) + mod
		rolls.append(roll)
	for number in rolls:
		result += str(number) + " "
		total += number
	result += " - TOTAL: " + str(total)
	print(result)