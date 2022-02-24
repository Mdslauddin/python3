class calculate():
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def add(self):
		return self.a+self.b
	def  sub(self):
		return self.a-self.b
	def mul(self):
		return self.a*slef.b
	def div(self):
		return self.a/self.b

a=int(input (	" enter first no :	"))
b=int(input(     " enter second no :	"))
obj=calculate(a,b)
choice =1
while choice !=0:
	print("0. Exit ")
	print("1. Add")
	print("2. Sun")
	print("3. Mul")
	print("4. Div")
	
	choice=int(input(" enter choice "	))
	if choice ==1:
		print("Result is :\t",obj.add())
		print("___________")
	elif choice==2:
		print("Result is :\t ",obj.sub())
		print("____________")
	elif choice==3:
		print("Result is :\t",obj.mul())
		print("_____________")
	elif choice==4:
		print("Result is:	\t", obj.div())
		print("_____________")
	elif choice==0:
		print("Exiting")
	else:
		print("Invalid choice !!")					