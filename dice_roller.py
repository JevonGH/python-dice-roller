import random

min = 1
max = 6

rolls = 0

while rolls < 6:
	print ("Rolling the dice...")
	print ("The result is: ", random.randint(min, max))
	rolls += 1