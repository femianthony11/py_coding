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
        self.real = a
        self.imag = b

    def magn(self):
        xy = self.real**2 + self.imag**2
        xyz = abs(sqrt(xy))
        return xyz



    def conj1(self,real,imag):
        conjnum = ComplexNumber(self.real,-self.imag,)
        return conjnum
# Check if self.imag is negative!

    def __add__(self,other):
        addi =  ComplexNumber(self.real+other.real, self.imag+other.imag)
        return addi
    def __sub__(self, other):
        sub = ComplexNumber(self.real-other.real, self.imag-other.imag)
        return sub
    def __mul__(self, other):
        mul = ComplexNumber(self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real)
        return mul
    def __div__(self, other):
            try: 
                return ComplexNumber(self.__mul__(other.real, -1*other.imag).__mul__(1.0/(other.mod().real)**2, 0))
            except Exception as e:
                print('error')
    
    def cmp(self,other):
            # Check the suits
            if self.magn() > other.magn:
                return 1
            if self.magn() < other.magn:
                return -1
            # Ranks are the same... it's a tie
            return 0

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0

    def __str__(self):
        if int(self.imag) == 0:
            print(self.real)
            quit()
        if int(self.imag) < 0:
            return (str(self.real)+ str(self.imag)+"i")
        else:
            return (str(self.real) +"+" + str(self.imag)+"i")
def op(ope):
    return (f"Operation = {ope}")



def main():
    arg1 = int((input("Enter number 1(Real): ")))
    arg2 = int((input("Enter number 1(Imaginary): ")))
    arg3 = int((input("Enter number 2(Real): ")))
    arg4 = int((input("Enter number 2(Imaginary: ")))
    arg5 = input("Enter Operation( + , - , x, /,<= ,>=,==,!=,<,> ) : ")



    

    complex1 = ComplexNumber(arg1,arg2)
    magnitude = complex1.magn()
    conjugate = complex1.conj1(arg1,arg2)
    complex2 = ComplexNumber(arg3,arg4)
    numi = complex1
    numi = str(numi)
    numi = numi.replace("i","j")
    numi = complex(numi)

    numii = (complex2)
    numii = str(numii)
    numii = numii.replace("i","j")
    numii = complex(numii)

    print(f"Magnitude = {magnitude}")
    print(f" Conjugate = {conjugate}")

    if (arg5 == '+'):
        print(complex1+complex2)
    elif (arg5 == '-'):
        print(complex1-complex2)
    elif (arg5 == 'x'):
        print(complex1*complex2)
    elif (arg5 == '/'):
        print((complex1)/(complex2))
    if arg5 == "<=":
        print(op(complex1 <= complex2))
    elif arg5 == "<":
        print(complex1 < complex2)
    elif arg5 == "==":
        print(complex1 == complex2)
    elif arg5 == ">":
        print(complex1 > complex2)
    elif arg5 == ">=":
        print(complex1 >= complex2)
    elif arg5 == "!=":
        print(complex1 != complex2)

if __name__ == "__main__":
    main()