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

        self.oplist = {"z1+z2":"4+6i"}


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
            arg1 = 1
            arg2 = 2
            arg3 = 3
            arg4 = 4
            
            a1 = '-'
            z1 = ComplexNumber(arg1,arg2)
            z2 =  ComplexNumber(arg3,arg4)
            z1 = str(z1)
            z2 = str(z2)

            z1 = z1.replace("i","j")
            z2 = z2.replace("i","j")

            z1 = complex(z1)
            z2 = complex(z2)
            print(z1)
            print(z2)

            if (a1 == '+'):
                z3 = z1+z2
                z3 = str(z3)
                z3 = z3.replace("j","i")
        

                
            

            if (a1 == '+'):
                z3 = z1+z2
                res = str(z3)
                res = res.replace("1","")
                res = res.replace("(","")
                res = res.replace(")","")
                res = res.replace("j","i")
            elif (a1 == '-'):
                z3 = z1-z2
                res = str(z3)
                res = res.replace("(","")
                res = res.replace(")","")
                res = res.replace("j","i")
            elif (a1 == '*'):
                z3 = z1*z2
                res =str(z3)
                res = res.replace("(","")
                res = res.replace(")","")
                res = res.replace("j","i")
            elif (a1 == '/'):
                z3 = z1/z2
                res =str(z3)
                res = res.replace("(","")
                res = res.replace(")","")
                res = res.replace("j","i")
    
            self.assertEqual(res,self.oplist[item])



if __name__ == "__main__":
    unittest.main()