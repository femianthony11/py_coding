import numpy as np
import math
from math import sqrt

def isInt(n):
    try: 
        int(n)
        return True
    except ValueError:
        return False



arg1 = (input("Enter number 1: "))
arg2 = (input("Enter number 2: "))

#if isInt(arg1) == False:
#    print("PLEASE INPUT NUMBER")
#    quit()
#elif isInt(arg1) == False:
#
#    quit()

arg1 = int(arg1)
arg2 = int(arg2)
class ComplexNumber:


    def __init__(self,a,b):
        self.a = a
        self.b = b 

    def magn(self):
        xy = self.a**2 + self.b**2
        xyz = abs(sqrt(xy))
        return xyz



    def conj1(self):
        conjnum = ComplexNumber(self.a, -self.b)


        return conjnum
# Check if self.b is negative!
    def __str__(self):
        if int(self.b) < 0:
            return (str(self.a)+ str(self.b)+"i")
        else:
            return (str(self.a) +"+" + str(self.b)+"i")

compnum = ComplexNumber(arg1,arg2)

magnitude = compnum.magn()
conjugate = compnum.conj1()

print(magnitude)
print(conjugate)