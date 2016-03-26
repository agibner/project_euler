import math

found = False;
num = 3;
count = 1;
prime = 2;
while not found:
	for x in range(2,int(math.ceil(math.sqrt(num)))+1):
		if num%x == 0:
			break
		if x == int(math.ceil(math.sqrt(num))):
                        print "found a prime!", num
			prime = num
			count = count+1
	if count == 10001:
		found = True
	num = num+2

print count
print prime
