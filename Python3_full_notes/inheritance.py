class empersonalinfo():
	def printdetails(self):
		print(f"employ name is :{self.empname} and employ id is :{self.empid}")
		
class salary(empersonalinfo):
	
	def calculatesalary(self):
	       
	       onedaysalary=self.basicsalary/30
	       workingdays=30 - self.leave
	       totsalary=onedaysalary * workingdays
	       print("your salary is : ",totsalary)
    	   
       
rahul=salary()
rahul.basicsalary=30000
rahul.leave=3
rahul.empid=101
rahul.empname="Rahul"


rahul.printdetails()
rahul.calculatesalary()	  
	
					