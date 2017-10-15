# 10_class.py

class Employee:
	totalEmployee = 0
	def __init__(self,name,salary):
		self.name = name
		self.salary =  salary
		self.salary_after_tax = 0
		self.salaryAfterPension = 0
		self.pension = 0.2
		self.deduceTax()

		Employee.totalEmployee += 1


	def displayMyInfo(self):
		print("Name: ",self.name)
		print("Salary: ",self.salary)

	def deduceTax(self):
		self.salary_after_tax =  self.salary - self.salary*0.36

	def __del__(self):
		print("Deleting ",self.name)
		Employee.totalEmployee = Employee.totalEmployee - 1


Jack = Employee("Jack",10000)

Felix = Employee("Felix Anderson",20000)

Jack.displayMyInfo()
print(Jack.salary_after_tax)

Felix.displayMyInfo()
print(Felix.salary_after_tax)



print(Employee.totalEmployee)

del(Jack)



print(Employee.totalEmployee)