class Math:
    def __init__(self, num):
        self.num = num

    def addToNum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a+b

# result = Math.add(5, 6)
# print(result)
a = Math(5)
print(a.num)
a.addToNum(6)
print(a.num)