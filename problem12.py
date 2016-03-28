import math

num_divisors = input("Number of divisors (greater than 3): ")
fulfilled = False
num = 3
trinum = 3
while not fulfilled:
	trinum = trinum + num
	num = num+1
	divisors = 0
	for x in range(1,int(math.ceil(math.sqrt(trinum)+1))):
		if trinum%x == 0:
                        if x == int(math.ceil(math.sqrt(trinum))):
                            divisors += 1
			else: 
                            divisors += 2
	if divisors > num_divisors:
		fulfilled = True
	
print trinum
