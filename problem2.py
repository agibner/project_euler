# Even Fibonacci numbers

fibs = [None] * 300
fibs[0] = 1
fibs[1] = 2
result = 2
curr = 2
index = 1

while curr <= 4000000:
    curr = fibs[index] + fibs[index-1]
    index = index + 1
    fibs[index] = curr
    if curr%2 == 0:
	result = result + curr
print result
