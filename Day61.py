# Inheritance in Python
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def showDetails(self):
        print(f"The name of Employee {self.id}: {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python.")

emp1 = Employee("Rohan", 69)
emp1.showDetails()
# emp1.showLanguage()
emp2 = Programmer("Akash", 7)
emp2.showDetails()
emp2.showLanguage()