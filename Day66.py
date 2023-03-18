class Employee:
    companyName = "Apple"           # Class Variable
    def __init__(self, name):
        self.name = name            
        self.raiseAmount = 0.02     # Instance Variable
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the {self.companyName}'s raise amount is {self.raiseAmount}.")

emp1 = Employee("Harry")
emp1.raiseAmount = 0.04
emp1.companyName = "Apple India"
emp1.showDetails()
# Employee.showDetails(emp1)
emp2 = Employee("Rohan")
emp2.showDetails()