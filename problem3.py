import math

def find_primes_to(final):
    found = False;
    num = 1
    pfactors = []
    # Loops until you reach the end number
    while not found:
	num = num+1
	# For each number, check whether it's prime
        for x in range( 2, int(math.ceil(math.sqrt(num)))+1 ):
            if num%x == 0:
                break
	    # If it has no factors but itself -> prime
            if x == math.ceil(math.sqrt(num)):
		# is it a factor of the original number?
		if final % num == 0:
		    pfactors.append(num)
                break
        if num >= math.sqrt(final):
                found = True
    print pfactors


find_primes_to(600851475143)
