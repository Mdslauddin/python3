# ValueError  6/h
#try:
#	a=int(input("enter 1st no : "))
#	b=int(input("enter 2nd no :"))
#	c=a/b
#	print(c)
#except ValueError:
#	print( "Error ! please input number only")
#else:
#	print("Thanks you...")	



#ArithmeticError   6/0
#try:
#	a=int(input("enter 1st no "))
#	b=int(input("enter 2nd no "))
#	c=a/b
#	print(c) 
#except ArithmeticError:
#			print("Error! divide by zero not allowed")
#else:
#	print("thank you...")							




#try:
#	saving=20000
#	withdrawal=10000
#	if withdrawal > saving :
#			raise exception()
#	else:
#			cash=saving-withdrawal
#except exception():
#			print("Not ! enough Balance !")
#else: 
#	print(withdrawal,"has been debited")
#	print("the available Balance is :",cash)	 
 
 
 # example -5
try:
 	fh=open("tesfile.txt","r")
 	fh.write("this is my file for exception handling ! ")
except IOError:
 	print("Error ! can't write data in file ")
else:
 	print("written content in the file successfully")		
 
 