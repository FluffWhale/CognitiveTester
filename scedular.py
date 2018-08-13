import grandpa
from datetime import datetime
import time

def finished():
	fout = open("info.txt","w+")
	fout.write("good")
	fout.close()

###Start
try:
	loop = 1
	print str(datetime.now())
	finished()
	while(loop == 1):
		ctime = datetime.now()
		if(ctime.hour == 21 and ctime.minute == 0 and ctime.second == 0):
			print "Begin Test"
			time.sleep(5)
			grandpa.Test()
			finished()
except:
	print "Oops something went wrong, trying again in 1 minute"
	time.sleep(60)


