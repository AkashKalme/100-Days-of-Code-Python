class Person:
    name = "Akash"
    age = 20
    occupation = "BE Undergrad"
    netWorth = 10000

    def info(self):
        print(f"{self.name} is a {self.occupation}.")

a = Person()
b = Person()
a.name = "Shubam"
a.occupation = "Player"
b.name = "Nitika"
b.occupation = "HR"
# print(a.name, a.occupation)
a.info()
b.info()