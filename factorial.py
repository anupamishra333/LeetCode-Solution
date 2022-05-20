def fact(n):

    if n ==0:
        return 1
    else:
        return n * fact(n-1)


# 
def factorial(n):
	
	res = 1
	
	for i in range(2, n+1):
		res = res * i
	return res

