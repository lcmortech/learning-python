# naive solution
def fib(n):
	if n == 1 or n == 2:
		result = 1
	else:
		result = fib(n-1) + fib(n-2)
	
	return result
	
	
print(fib(3))

#memoized solution
# memo is an array. length is n+1 to include the last item
# must be initialized before calling function
#T(n) = # of calls fib with the time is takes to execute
def fib_cache(n, memo): # fib called once <= (2n 
	if memo[n] is not None:
		return memo[n]
	if n ==1 or n==2:
		result = 1
		
	else:
		result = fib(n-1) + fib(n-2) # fib called a 2nd time (constant time - 2n -> n)
		
# bottom up solution

def fib_bu(n):
	if n ==1 or n == 2:
		result = 1
	bottom_up = new int[n + 1]
	bottom_up[1] = 1
	bottom_up[2] = 2
	for i in 3 up to n:
		bottom_up[i] = bottom_up[n-1] + bottom_up[n-2]
		return bottom_up[n]
