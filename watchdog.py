from datetime import datetime
import time

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

def check():
	try:
		fin = open("info.txt","r")
		line = fin.readlines()
		fin.close()
		if(line[0] == "good"):
			fout = open("info.txt","w+")
			fout.write("not good yet")
			fout.close()
		else:
			SendText("Test untaken after 30 mins!")
	except:
		SendText("Problem with file, notifie phil")

###Start
loop = 1
print str(datetime.now())
while(loop == 1):
	ctime = datetime.now()
	if(ctime.hour == 21 and ctime.minute == 30 and ctime.second == 0):
		check()
		time.sleep(5)
