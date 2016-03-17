m = 0;
sumsquared = 0;
for x in range(1,101):
	m = m+x;
for n in range(1,101):
	sumsquared = sumsquared + (n*n);

result = m*m - sumsquared;
print result
		
