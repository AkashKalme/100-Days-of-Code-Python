# Super Keyword

# class ParentClass:
#     def parent_method(self):
#         print("Parent Class' Parent Method.")

# class ChildClass(ParentClass):
#     def parent_method(self):
#         print("Child Class' Parent Method.")
#         super().parent_method()
#     def child_method(self):
#         print("Child Class' Child Method.")
#         self.parent_method()
#         super().parent_method()

# obj1 = ChildClass()
# obj1.child_method()

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

rohan = Employee("Rohan Das", 451)
harry = Programmer("Harry J", 787, "Python")
print(rohan.name, rohan.id)
print(harry.name, harry.id, harry.lang)

