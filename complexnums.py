import numpy as np
import math
from math import sqrt


arg1 = 1
arg2 = 2

arg3 = 1+2j

class ComplexNumber:


    def __init__(self,x,y,z):
        self.x = x
        self.y = y 
        self.z = z

    def magn(self):
        xy = self.x**2 + self.y**2
        xyz = abs(sqrt(xy))
        return xyz



    def conj1(self):
        conjnum = np.conj(self.z)
        conjnum = str(conjnum)
        num = str(self.z)
        return "The conjugation of " + num + " = " + conjnum


compnum = ComplexNumber(arg1,arg2,arg3)
print(compnum.magn())
print(compnum.conj1())