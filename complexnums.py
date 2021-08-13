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
        sub = self.real-other.real, self.imag-other.imag
        return sub
    def __mul__(self, other):
        mul = self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real
        return mul
    def __div__(self, other):
            try: 
                return self.__mul__(other.real, -1*other.imag).__mul__(1.0/(other.mod().real)**2, 0)
            except Exception as e:
                print('error')
    def __str__(self):
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
    arg5 = input("Enter Operation( + , - , x, /) : ")



    

    compnum = ComplexNumber(arg1,arg2)
    magnitude = compnum.magn()
    conjugate = compnum.conj1(arg1,arg2)
    other = ComplexNumber(arg3,arg4)
    
    numi = compnum
    numi = str(numi)
    numi = numi.replace("i","j")
    numi = complex(numi)

    numii = (other)
    numii = str(numii)
    numii = numii.replace("i","j")
    numii = complex(numii)


    add = compnum + other
    add = str(add)
    add = add.replace("j","i")
    
    sub = compnum - other
    sub = str(sub)
    sub = sub.replace("j","i")
    
    mul = compnum * other
    mul = str(mul)
    mul = mul.replace("j","i")
    
    div = numi / numii
    div = str(div)
    div = div.replace("j","i")
    div = div.replace("(","")
    div = div.replace(")","")
    print(f"Magnitude = {magnitude}")
    print(f" Conjugate = {conjugate}")

    if (arg5 == '+'):
        print(op(add))
    elif (arg5 == '-'):
        print(op(sub))
    elif (arg5 == 'x'):
        print(op(mul))
    elif (arg5 == '/'):
        print(op(div))
    


if __name__ == "__main__":
    main()