import numpy as np
import math
import complexnums
from complexnums import ComplexNumber
from complexnums import *
from math import sqrt
import unittest


class compTest(unittest.TestCase):

    def setUp(self):
        self.conjlist = {   
                "1,2":"1-2i", 
                "3,8":"3-8i", 
                "9,4":"9-4i", 
                "6,2":"6-2i"}
        self.magnlist = {   
                "1,2":"2.23606797749979", 
                "3,8":"8.54400374531753", 
                "9,4":"9.848857801796104", 
                "6,2":"6.324555320336759"}

        self.oplist = {"z1+z2":"9+i","z1-z2":"1+5i","z1*z2":"26+2i"}


    def test_fact(self):

        for item in self.magnlist:
            arg1 = int(item[0])
            arg2 = int(item[2])
            cn = ComplexNumber(arg1,arg2)
            magnitude = cn.magn()
            print(magnitude)
            res = str(magnitude)
            self.assertEqual(res,self.magnlist[item])

        for item in self.conjlist:
            arg1 = int(item[0])
            arg2 = int(item[2])
            cn = ComplexNumber(arg1,arg2)
            conjugate = cn.conj1(arg1,arg2)
            print(conjugate)
            res = str(conjugate)
            self.assertEqual(res,self.conjlist[item])
        for item in self.oplist:
            z1 = ("5+3i")
            z2 = ("4-2i")
            a1 = item[2]
            n1 = int(z1[0])
            n2 = int(z1[2])
            n3 = int(z2[0])
            n4 = -(int(z2[2]))
            ans = ComplexNumber(n1,n2)
            add = ans.__add__(n3,n4)

            sub = ans.__sub__(n3,n4)
            mul = ans.__mul__(n3,n4)
            

            if (a1 == '+'):
                res = str(add)
                res = res.replace("1","")
                res = res.replace("(","")
                res = res.replace(")","")
                res = res.replace("j","i")
            elif (a1 == '-'):
                res = str(sub)
                res = res.replace("(","")
                res = res.replace(")","")
                res = res.replace("j","i")
            elif (a1 == '*'):
                res =str(mul)
                res = res.replace("(","")
                res = res.replace(")","")
                res = res.replace("j","i")
    
            self.assertEqual(res,self.oplist[item])



if __name__ == "__main__":
    unittest.main()