#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here:
def Generar():
    arr = []
    for i in range(10):
        nint = random.randint(1,100)
        arr.append(nint)
    return arr

my_list.extend(Generar())
my_list.sort()

print(my_list[:])