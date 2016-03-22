import math

# Parameters -  num is a positive integer
def prime_factorization(num):
    curr = num
    factors = {}
    while curr % 2 == 0:
        if not 2 in factors: 
            factors[2] = 1
        else:
            factors[2] = factors[2] + 1
        curr = curr/2

    divisor = 3
    while curr > 1:
        if curr % divisor == 0:
            curr = curr/divisor
            if not divisor in factors:
                factors[divisor] = 1
            else:
                factors[divisor] = factors[divisor] + 1
        else: 
            divisor = divisor + 2

    return factors

# Will find the lcm of num and all numbers below > 0. 
def lcm(num):
    lcm_factors = {}
    for x in xrange(2, num+1):
        factors = prime_factorization(x)
        for f in factors:
            if f in lcm_factors:
                lcm_factors[f] = max(factors[f], lcm_factors[f])
            else:
                lcm_factors[f] = factors[f]

    product = 1
    for n in lcm_factors:
        for x in xrange(lcm_factors[n]):
            product = product*n

    return product

print lcm(10)
print lcm(20)
