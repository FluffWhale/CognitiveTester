import random
from gpiozero import LED
from gpiozero import Button
from twilio.rest import Client
import os
import time

class flag:
	question = ' '
	badAnswer = ' '
	weight = 0

def Flag(question,badAnswer,weight):
	tmp = flag()
	tmp.question = question
	tmp.badAnswer = badAnswer
	tmp.weight = weight
	flags.append(tmp)

def SendText(content):
	# Your Account SID from twilio.com/console
	account_sid = "AC03564db51bb5442f01d09bf7644f3289"
	# Your Auth Token from twilio.com/console
	auth_token  = "60e0d7a70fb9d734e05cd97c8d9d379c"
	
	client = Client(account_sid, auth_token)
	
	message = client.messages.create(
	    to="+18655665431", 
	    from_="+18652696318",
	    body=content)

	print(message.sid)

def AlertPhil(content):
	# Your Account SID from twilio.com/console
	account_sid = "AC03564db51bb5442f01d09bf7644f3289"
	# Your Auth Token from twilio.com/console
	auth_token  = "60e0d7a70fb9d734e05cd97c8d9d379c"
	
	client = Client(account_sid, auth_token)
	
	message = client.messages.create(
	    to="+18652552013", 
	    from_="+18652696318",
	    body=content)

	print(message.sid)

def MathQuestion():
	trys =  0 
	randNums = []
	key = [" + ", " - ", " * "]
	answer = 0
	randNums.append(random.randint(0,2))
	randNums.append(random.randint(1,11))
	randNums.append(random.randint(1,11))
	
	if(randNums[0]==0):
		#while(input not right):
		userAnswer = input("What is " + str(randNums[1]) + key[randNums[0]]+ str(randNums[2]) +" =\n")
		answer = randNums[1] + randNums[2] 
	if(randNums[0]==1):
		userAnswer = input("What is " + str(randNums[1]) + key[randNums[0]]+ str(randNums[2]) +" =\n")
		answer = randNums[1] - randNums[2] 
	if(randNums[0]==2):
		userAnswer = input("What is " + str(randNums[1]%5) + key[randNums[0]]+ str(randNums[2]%5) +" =\n")
		answer = (randNums[1]%5 )* (randNums[2]%5)
	if(str(userAnswer) == str(answer)):
		print("Correct!\n")
	else:
		while(str(userAnswer) != str(answer) and trys < 3):
			trys += 1
			Flag(("What is " + str(randNums[1]) + key[randNums[0]]+ str(randNums[2]) +" (If multiplication then actual numbers = nums%5)"),str(userAnswer),1)
			userAnswer = input("Try Again\n")
		if(trys == 3):
			print("Out of tries")
		else:
			print("Correct!\n")

def CatQuestion():
	cats = [["John","Samual","Adam","Robert","Alice","JoAnn","Marry","Karen"],["Lunch","Box","Tractor","Book"],["Blue","Red","Green","Purple","Brown","Grey","Yellow","Pink"],["Tree","Cat","Deck","Car"]]
	randNums = []
	values = []
	noOrder = ["*","*","*"]
	counter = 0
	answer = ""
	i = 0
	randNums.append(random.randint(0,1))
	randNums.append(random.randint(0,7))
	randNums.append(randNums[1])
	while(randNums[1] == randNums[2]):
		randNums[2] = random.randint(0,7)
	randNums.append(random.randint(0,3))
	values.append(cats[randNums[0]*2][randNums[1]])
	values.append(cats[randNums[0]*2][randNums[2]])
	values.append(cats[randNums[0]*2+1][randNums[3]])
	noOrder[random.randint(0,2)] = values[2]
	for value in noOrder:
		if(value == "*"):
			noOrder[i] = values[counter]
			counter += 1
		i += 1
	if(randNums[0] == 0):
		userAnswer = input("What is not a person's NAME: " +  noOrder[0] + " or " + noOrder[1] + " or " + noOrder[2] +"?\n")
	else:
		userAnswer = input("What is not a COLOR: " +  noOrder[0] + " or " + noOrder[1] + " or " + noOrder[2] +"?\n")
	if(userAnswer.lower() == values[2].lower()):
		print("Correct!")
	else:
		while(userAnswer.lower() != values[2].lower()):
			if(userAnswer.lower() == values[0].lower() or userAnswer.lower()== values[1].lower()):
				Flag(("Catagory Question: " +  values[0] + " or " + values[1] + " or " + values[2]),userAnswer,1)
				userAnswer = input("Wrong, try again.\n")
			else :
				Flag(("Possible error in Catagory Question: " +  values[0] + " or " + values[1] + " or " + values[2]),userAnswer,0)
				userAnswer = input("Not an option, try again.\n")

######Main Function
def Test():
	os.system('clear')
	weights = 0
	warning = "\n"
	MathQuestion()
	time.sleep(3)
	os.system('clear')
	CatQuestion()
	time.sleep(3)
	os.system('clear')
	MathQuestion()
	time.sleep(3)
	os.system('clear')
	for i in flags:
		weights += i.weight
	if weights > 1:
		for i in flags:
			warning += "Question was: " + i.question + "\nIncorrect Answer was: " + i.badAnswer + "\n"
		print(warning)
		#SendText(warning)
		print("Text Sent")
	else:
		print("You passed!")
	flags[:] = []
######Start of program
button = Button(2)
led = LED(17)
flags = []
#try:
Test()
#except:
#	print("Problem with program, Philip notified")
	#AlertPhil("Test Failed in Some way")

