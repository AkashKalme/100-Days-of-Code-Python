# Access Modifiers in Python
# class Employee:
#     pass

# a = Employee()
# a.emp1 = 5

# Public
# class Employee:
#     def __init__(self):
#         self.name = "Akash"

# a = Employee()
# print(a.name)

# Private
# Variables are declared with Double Underscore(__)
# class Employee:
#     def __init__(self):
#         self.__name = "Akash"

# a = Employee()
# # print(a.__name)   # Error Raised
# print(a._Employee__name)
# print(a.__dir__)

# Protected
# Variables are declared with Single Underscore(_)
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())