# Class and Objects in Python
class Person:
    def __init__(self, n, o):
        print("Hey there!")
        self.name = n
        self.occupation = o

    def info(self):
        print(f"{self.name} is a {self.occupation}.")

a = Person("Akash", "SDE")
a.info()
b = Person("Divya", "HR")
b.info()