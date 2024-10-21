def factorial(n):
	if n==0 or n==1:
		return 1
	result=factorial(n-1)
	return n*result
number=int(input("enter a number to find its factorial:"))
print("the factorial of",number,"is",factorial(number))
