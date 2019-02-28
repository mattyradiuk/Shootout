#Matt Radiuk
#2019

import random
import os
import time

clear = lambda: os.system('cls')

# Current selection of teams, more to come!!!
real = [("Bale", 89), ("Isco", 82), ("Modric", 86), ("Ramos", 82), ('Vincinius Jr', 72), ("Navas", 72)]

barca = [("Messi", 90), ("Coutinho", 87), ("Dembele", 83), ("Suarez", 86), ("De Jong", 73), ("Ter Stegen", 74)]

bayern = [("Lewandowski", 91), ("Muller", 86), ("James", 87), ("Robben", 86), ('Davies', 66), ("Neuer", 70)]

juve = [("Ronaldo", 94), ("Dybala", 84), ("Douglas", 82), ("Mandjukic", 80), ('Pjanic', 82), ("Buffon", 76)]

spurs = [("Kane", 88), ("Eriksen", 87), ("Son", 84), ("Dele", 81), ('Lucas', 82), ("Lloris", 75)]

united = [("Pogba", 84), ("Lingard", 82), ("Rashford", 81), ("Lukaku", 76), ('Martial', 81), ("De Gea", 80)]

liverpool = [("Salah", 87), ("Milner", 80), ("Firmino", 83), ("Shaqiri", 75), ('Oxlade-Chamberlain', 80), ("Alison", 77)]

city = [("Aguero", 87), ("Sterling", 82), ("De Bruyne", 88), ("Sane", 80), ('Jesus', 74), ("Ederson", 68)] 

chelsea = [("Higuian", 83), ("Pedro", 82), ("Hazard", 88), ("Willian", 80), ('Loftus-Cheek', 77), ("Kepa", 65)]

arsenal = [("Aubameyang", 84), ("Lacazette", 85), ("Iwobi", 79), ("Ozil", 85), ('Torreria', 74), ("Leno", 69)]

custom = []
goalsNum = 0
opoGoals = 0

def main():
	myTeam, opoTeam = intro()
	play(preMatchToss(), myTeam, opoTeam)
	endGame()


def intro():
    # Intro to the game and team selection
	print("120 minutes have passed but the game is still tied")
	time.sleep(0.3)
	print("It is going to come down to the penalty shootout!!!")
	time.sleep(1)
	print("")
	time.sleep(.5)
	print("Teams:\n Real Madrid 84\n Barcelona 85\n Bayern Munich 83\n Juventus 84\n Man United 81\n Man City 82\n Liverpool 81\n Tottenham Hotspur 83\n Custom\n")

	myTeam = []
	opoTeam = []

	#Pick the team you control
	while(1):
		teamChoose = input("Which team would you like to be?: ")
		print("")
		if(teamChoose.lower() in ("real", "real madrid", "madrid")):
			myTeam = real
			break
		if(teamChoose.lower() in ("barca", "barcelona", "fcb")):
			myTeam = barca
			break
		if(teamChoose.lower() in ("bayern", "munich")):
			myTeam = bayern
			ibreak
		if(teamChoose.lower() in ("juve", "juventus")):
			myTeam = juve	
			break
		if(teamChoose.lower() in ("spurs", "tottenham")):
			myTeam = spurs	
			break
		if(teamChoose.lower() in ("united", "man utd")):
			myTeam = united	
			break
		if(teamChoose.lower() in ("liverpool", "lfc")):
			myTeam = liverpool	
			break
		if(teamChoose.lower() in ("city", 'man city', 'manchester city')):
			myTeam = city
			break
		if(teamChoose.lower() in ("arsenal", 'gunners')):
			myTeam = arsenal
			break
		if(teamChoose.lower() in "custom"):
			myTeam = custom
			customFill()	
		print("Input was invalid, please try again")
	print("This is how your team lines up")
	print("----------------")
	for (name, rating) in myTeam:
		print(name, rating)
	print("----------------\n")

	#Pick the team the AI controls
	while(1):
		opoChoose = input("Which team would you like to face?: ")
		print("")
		if(opoChoose.lower() in ("real", "real madrid", "madrid")):
			opoTeam = real
			break
		if(opoChoose.lower() in ("barca", "barcelona")):
			opoTeam = barca
			break
		if(opoChoose.lower() in ("bayern", "bayern munich", "munich")):
			opoTeam = bayern
			break
		if(opoChoose.lower() in ("juve", "juventus")):
			opoTeam = juve	
			break
		if(opoChoose.lower() in ("spurs", "hotspur", "tottenham")):
			opoTeam = spurs	
			break
		if(opoChoose.lower() in ("united", "utd", "man united", "man utd")):
			opoTeam = united	
			break
		if(opoChoose.lower() in ("liverpool", "lfc")):
			opoTeam = liverpool	
			break
		if(opoChoose.lower() in ("city", 'man city', 'manchester city')):
			opoTeam = city
			break
		if(opoChoose.lower() == "custom"):
			opoTeam = custom
			customFill()	
		print("Input was invalid, please try again\n")
	print("This is how the other team lines up")
	print("----------------")
	for (name, rating) in opoTeam:
		print(name, rating)
	print("----------------\n")	
	playQ = input("If you're happy with the teams, type 'play', anything else will restart team selection: ")
	if(playQ.lower() != "play"):
		main()
	clear()
	return myTeam, opoTeam

def preMatchToss():
	print("First / Second / Random")
	while(1):
		choice2 = input("Would you shoot first second or random?: ")
		if(choice2.lower() in ("first", "f", "frist", "1")):	
			return(0)
		if(choice2.lower() in ("second", "s", "sec", "2")):	
			return(1)
		if(choice2.lower() in ("random", 'r', 'rand')):	
			toss = int(random.randint(0,1))
			if(toss == 0):
				print("You have won the toss and will kick first!")
				time.sleep(1)
				print("")
				return(0)
			if(toss == 1):
				print("You have lost the toss and will shoot second")
				time.sleep(1)
				print("")
				return(1)
		print("Input was invalid, please try again\n")

def customFill():
    #When you select "custom" at kickoff
	for i in range(1, 6):
		customPlayer = input("Enter name for player " + str(i) + ": ")
		customRating = input("Enter rating for player " + str(i) + ": ")
		custom.append((customPlayer,int(customRating)))
	customGoalie = input("Enter name for goalie: ")
	customGRating = input("Enter rating for goalie: ")
	custom.append((customGoalie,int(customGRating)))

def play(x, myTeam, opoTeam):
	if(x == 0):
		for i in range(4):
			myTeamShot(i, myTeam[i])
			opoTeamShot(i, opoTeam[i])
			#TODO: EndGame Scenarios!!!
	if(x == 1):
		for i in range(4):
			opoTeamShot(i, opoTeam[i])
			myTeamShot(i, myTeam[i])

def myTeamShot(shooterNum, shooter):
	#Globals required for keeping score
	global goalsNum
	global opoGoals
	print("The score is " + str(goalsNum) + " - " + str(opoGoals))
	print("The shooter is " + shooter[0] + " and his rating is " + str(shooter[1]))
	print("")
	print("Left / Middle / Right")
	shotAtmpt = input("Where would you like to shoot?: ")
	shotPlace = -1
	AIgoalie = int(random.randint(0,2))
	if(shotAtmpt.lower() in ("left", "l")):
		shotPlace = 0
	if(shotAtmpt.lower() in ("mid", "m")):
		shotPlace = 1
	if(shotAtmpt.lower() in ("right", "r")):
		shotPlace = 2
	if(shotPlace == -1):
		print("Shot selection is invalid")
		print(shooter[0] + " looks shaken and rolls it softly down the middle")
		shotPlace = 1
	print("").
	
	if(AIgoalie == 0):
		print("Goalie dives left!")
	if(AIgoalie == 1):
		print("Goalie stands his ground!")
	if(AIgoalie == 2):
		print("Goalie dives right!")
	print("And it is a")
	for i in range(0,3):
		time.sleep(0.6)
		print(".")
	time.sleep(1)
	if(shotPlace == AIgoalie):
		a = random.randint(1, 15)
		if(a < (100 - shooter[1])):
			print("SAVE!")
			time.sleep(.8)
			print("The score remains " + str(goalsNum) + " - " + str(opoGoals))
			time.sleep(1.7)
		else:
			print("GOAL!")
			goalsNum = goalsNum + 1
			time.sleep(0.8)
			print(shooter[0] + " scores to make it " + str(goalsNum) + " - " + str(opoGoals))
			time.sleep(1.7)
	if(shotPlace != AIgoalie):
		a = random.uniform(1, 100)
		if(a < (100 - shooter[1])):
			print("COMPLETE SHANK! HE MISSED THE NET")
			time.sleep(.8)
			print("The score remains " + str(goalsNum) + " - " + str(opoGoals))
			time.sleep(1.7)
		elif(a < (100 - shooter[1]) + 10):
			print("MISS! HE RIPPED IT OFF OF THE POST AND OUT")
			time.sleep(.8)
			print("The score remains " + str(goalsNum) + " - " + str(opoGoals))
			time.sleep(1.7)
		else:
			print("GOAL!")
			goalsNum = goalsNum + 1
			time.sleep(.8)
			print(shooter[0] + " scores to make it " + str(goalsNum) + " - " + str(opoGoals))
			time.sleep(1.7)
	shooterNum = shooterNum + 1
	clear()
	

def opoTeamShot(shooterNum, shooter):
	global goalsNum
	global opoGoals
	print("The score is " + str(goalsNum) + " - " + str(opoGoals))
	print("The shooter is " + shooter[0] + " and his rating is " + str(shooter[1]))
	print("")
	print("Left / Midddle / Right")
	saveAtmpt = input("Which way would you like your goaie to dive?: ")
	savePlace = -1
	AIshooter = int(random.uniform(0,3))
	#print(AIgoalie)
	if(saveAtmpt.lower() in ("left", "l")):
		savePlace = 0
	if(saveAtmpt.lower() in ("mid", "middle", "m")):
		savePlace = 1
	if(saveAtmpt.lower() in ("right", "r")):
		savePlace = 2
	if(savePlace == -1):
		print("Keeper gets some bad instructions, he's frozen in place!")
		savePlace = 1
	print("")
	if(AIshooter == 0):
		print("He shoots it left!")
	if(AIshooter == 1):
		print("He shoots it right down the middle!")
	if(AIshooter == 2):
		print("He shoots it to the right!")
	print("And it is a")
	for i in range(0,3):
		time.sleep(0.6)
		print(".")
	time.sleep(1)
	if(savePlace == AIshooter):
		a = random.uniform(1, 18)
		if(a < (100 - shooter[1])):
			print("SAVE!")
			time.sleep(0.8)
			print("The score remains " + str(goalsNum) + " - " + str(opoGoals))
			time.sleep(1.7)
		else:
			print("GOAL!")
			opoGoals = opoGoals + 1
			time.sleep(.8)
			print(shooter[0] + " scores to make it " + str(goalsNum) + " - " + str(opoGoals))
			time.sleep(1.7)
	if(savePlace != AIshooter):
		a = random.uniform(1, 100)
		if(a < (100 - shooter[1])):
			print("COMPLETE SHANK! HE MISSED THE NET")
			time.sleep(0.8)
			print("The score remains " + str(goalsNum) + " - " + str(opoGoals))
			time.sleep(1.7)
		elif(a < (100 - shooter[1]) + 10):
			print("MISS! HE RIPPED IT OFF OF THE POST")
			time.sleep(0.8)
			print("The score remains " + str(goalsNum) + " - " + str(opoGoals))
			time.sleep(1.7)
		else:
			print("GOAL!")
			opoGoals = opoGoals + 1
			time.sleep(.8)
			print(shooter[0] + " scores to make it " + str(goalsNum) + " - " + str(opoGoals))
			time.sleep(1.8)
	clear()
	
def endGame():
	global goalsNum
	global opoGoals
	print("Game over!")
	if(goalsNum > opoGoals):
		print("You win with a final score of " + str(goalsNum) + " - " + str(opoGoals))
		print("Would you like to play again?")
		print("")
		restart = input("Y / N: ")
		if(restart.lower() == "y"):
			clear()
			main()
		else:
			print("Thank you for playing.")
			print("Copyright © Matt Radiuk 2018")
			time.sleep(6)
			exit()
	if(goalsNum < opoGoals):
		print("The machine wins with a final score of " + str(goalsNum) + " - " + str(opoGoals))
		print("Would you like to play again?")
		restart = input("Y / N: ")
		if(restart.lower() == "y"):
			clear()
			main()
		else:
			print("Thank you for playing.")
			print("Copyright © Matt Radiuk 2018")
			time.sleep(6)
			exit()
	if(goalsNum == opoGoals):
		print("The score is tied " + str(goalsNum) + " - " + str(opoGoals))
		print("Would you like to play again?")
		restart = input("Y / N: ")
		if(restart.lower() == "y"):
			clear()
			main()
		else:
			print("Thank you for playing.")
			print("Copyright © Matt Radiuk 2019")
			time.sleep(6)
			exit()
if __name__ == '__main__':
	main()
