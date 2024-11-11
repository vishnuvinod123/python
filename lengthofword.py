a=[]
n=int(input("enter the number of element:"))
for x in range(0,n):
	element=input("enter the element"+str(x+1)+":")
	a.append(element)
max1=len(a[0])
temp=a[0]
for i in a:
	if(len(i)>max1):
		max1=len(i)
		temp=i
print("the langest length is:")
print(temp)
