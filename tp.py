import math

def bs(sorted_table, element):
    index = math.ceil(len(sorted_table)/2)
    while(element!=sorted_table[index]):
        if(sorted_table[index]>element):
            index = math.ceil(index/2)
        else:
            index = math.ceil(index + index/2)
    return index

sorted_table = []
print(bs(sorted_table, 9))