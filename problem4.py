import math

def isPallindrome(string):
    length = len(string)
    for x in xrange(length/2):
        if string[x] != string[length-x-1]:
            return False
    return True

def findLargestPallindromeBelow(num):
    start = num
    INTERVAL = 100
    found = False
    while not found:
        for a in xrange(start, start-INTERVAL, -1):
            for b in xrange(a, start-INTERVAL, -1):
                product = str(a*b)
                if isPallindrome(product):
                    found = True
                    return (a, b)
        start = start-INTERVAL

a, b = findLargestPallindromeBelow(1000)    
print a, b, a*b
