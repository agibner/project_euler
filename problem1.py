
sum = 0

for x in xrange(0,1000):
    if x%5 == 0:
	sum = sum + x
    elif x%3 == 0:
	sum = sum + x

print sum
