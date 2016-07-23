
# the separate thread will pause for the time.sleep calls. Meanwhile, your program can do other work in the original thread.

import threading, time
print ('Start of program')

def takeANAP():
	time.sleep(5)
	print('Wake up!')
	
threadObj = threading.Thread(target=takeANAP)
threadObj.start()

print('End of program.')