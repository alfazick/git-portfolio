#! python3
# stopwatch.py - A simple stopwatch program.

import time

# Display the program's instructions.
print('Press Enter to begin. Afterwards, press Enter to "click" the stopwatch. Press ctrl-C to quit.') 

input()  # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1 

# Start tracking the lap times.

try:
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		print('Lap #%s: %s (%s)' % (lapNum, totalTime,lapTime), end= '')
		lapNum += 1
		lastTime = time.time()  # reset the last lap time
except KeyboardInterrupt:
	# Handle the ctrl-c exception to keep its error message from displaying.
	print('\nDone.')