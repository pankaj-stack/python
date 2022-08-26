def add():
	a=float(input('Enter the first no. '))
	b=float(input('Enter the second no. '))
	return a+b

def sub():
	a=float(input('Enter the first no. '))
	b=float(input('Enter the second no. '))
	return a-b

def mul():
	a=float(input('Enter the first no. '))
	b=float(input('Enter the second no. '))
	return a*b
	
def div():
	a=float(input('Enter the first no. '))
	b=float(input('Enter the second no. '))
	return a/b
def factorial():
	f=1
	n=int(input('Enter the no. to find the factorial '))
	if n<2:
		return 1
	else:
		for i in range(n):
			f=n*f
			n-=1
		return f


