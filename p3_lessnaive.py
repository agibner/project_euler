import math

def find_largest_prime_factor(num):
    start = num
    found = False

    for x in xrange(2,num):
        if num % x == 0:
            curr = num / x
	    if is_prime(curr):
                found = True
		print curr
		return curr
            # The first prime factor you reach is the largest! 
	
def is_prime(num):
    for x in xrange(2, int(math.ceil(math.sqrt(num)))+1):
	if num%x == 0:
	    return False
	if x == math.ceil(math.sqrt(num)):
	    return True

print find_largest_prime_factor(13195)
print find_largest_prime_factor(600851475143)
