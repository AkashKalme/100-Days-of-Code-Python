def calculateGMean(a, b):
    gmean = (a*b)/(a+b)
    print(gmean)

def calculateGreater(a, b):
    if(a>b):
        print(a, "is greater.")
    else:
        print(b, "is greater or equal.")

def calculateLesser(a, b):
    pass



calculateGreater(8, 6)
calculateGMean(8, 6)