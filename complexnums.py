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

    def __add__(self,other):
        addi =  ComplexNumber(self.a+other.a, self.b+other.b)
        return addi
    def __sub__(self, other):
        sub = complex(self.a-other.a, self.b-other.b)
        return sub
    def __mul__(self, other):
        mul = complex(self.a*other.a-self.b*other.b, self.a*other.b+self.b*other.a)
        return mul
    def __div__(self, other):
            try: 
                return self.__mul__(complex(other.a, -1*other.b)).__mul__(complex(1.0/(other.mod().real)**2, 0))
            except Exception as e:
                print('error')
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
    arg5 = input("Enter Operation( + , - , x, /) : ")



    arg1 = int(arg1)
    arg2 = int(arg2)
    arg3 = int(arg3)
    arg4 = int(arg4)
    compnum = ComplexNumber(arg1,arg2,)
    numi = compnum
    numi = str(numi)
    numi = complex(numi.replace("i","j"))
    
    magnitude = compnum.magn()
    conjugate = compnum.conj1(arg1,arg2)
    other = ComplexNumber(arg3,arg4)

    numii = other
    numii = str(numii)
    numii = complex(numii.replace("i","j"))


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