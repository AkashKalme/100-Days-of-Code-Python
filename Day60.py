# Getters and Setters in Python
class MyClass:
    def __init__(self, val):
        self._value = val

    def show(self):
        print(f"Value is {self._value}")

    @property
    def tenValue(self):
        return 10*self._value

    @tenValue.setter
    def tenValue(self, new_value):
        self._value = new_value/10

a = MyClass(10)
a.tenValue = 85
a.show()
print(a.tenValue)