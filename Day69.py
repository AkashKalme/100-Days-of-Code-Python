# Class Methods in Python

class Employee:
    company = "Apple"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}.")
    
    def changeCompany(cls, newCompany):
        cls.company = newCompany

    @classmethod
    def changeCompanyC(cls, newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "Harry"
e1.show()
e1.changeCompany("Tesla")
print(Employee.company)
e1.show()
e1.changeCompanyC("Meta")
print(Employee.company)
e1.show()