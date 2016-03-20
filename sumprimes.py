from math import sqrt

def prime(number):
	for x in range(2, int(sqrt(number)+1)):
		if number % x == 0:	
			return False
	return True

num = 2;
sum = 0;
below = input("Sum of primes below: ")

while num<below:
	if prime(num):	
		sum = sum+num
	num = num+1
print sum
