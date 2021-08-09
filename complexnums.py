import numpy as np
import math
from math import sqrt

def isInt(n):
    try: 
        int(n)
        return True
    except ValueError:
        return False




class ComplexNumber:


    def __init__(self,a,b):
        self.a = a
        self.b = b

    def magn(self):
        xy = self.a**2 + self.b**2
        xyz = abs(sqrt(xy))
        return xyz



    def conj1(self,a,b):
        conjnum = ComplexNumber(self.a,-self.b,)
        return conjnum
# Check if self.b is negative!

    def __add__(self,other,other1):
        addi =  ComplexNumber(self.a+other, self.b+other1)
        return addi
    def __sub__(self, other,other1):
        sub = complex(self.a-other, self.b-other1)
        return sub
    def __mul__(self, other,other1):
        mul = complex(self.a*other-self.b*other1, self.a*other1+self.b*other)
        return mul
    def __str__(self):
        if int(self.b) < 0:
            return (str(self.a)+ str(self.b)+"i")
        else:
            return (str(self.a) +"+" + str(self.b)+"i")
def op(ope):
    return (f"Operation = {ope}")



def main():
    arg1 = (input("Enter number 1(Real): "))
    arg2 = (input("Enter number 1(Imaginary): "))
    arg3 = (input("Enter number 2(Real): "))
    arg4 = (input("Enter number 2(Imaginary: "))
    arg5 = input("Enter Operation( + , - , x) : ")



    arg1 = int(arg1)
    arg2 = int(arg2)
    arg3 = int(arg3)
    arg4 = int(arg4)
    compnum = ComplexNumber(arg1,arg2,)

    magnitude = compnum.magn()
    conjugate = compnum.conj1(arg1,arg2)
    add = compnum.__add__(arg3,arg4)
    sub = compnum.__sub__(arg3,arg4)
    mul = compnum.__mul__(arg3,arg4)
    print(f"Magnitude = {magnitude}")
    print(f" Conjugate = {conjugate}")

    if (arg5 == '+'):
        print(op(add))
    elif (arg5 == '-'):
        print(op(sub))
    elif (arg5 == 'x'):
        print(op(mul))
    


if __name__ == "__main__":
    main()