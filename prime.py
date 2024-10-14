lowervalue=int(input("enter the lower value:"))
highervalue=int(input("enter the higher value:"))
isprime=True
for number in range(lowervalue,highervalue+1):
	if number>1:
		isprime=True
		for i in range(2,number):
			if(number%i)==0:
				isprime=False
				break
	if isprime:
		print(number)
