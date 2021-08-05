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
            conjugate = cn.conj1()
            print(conjugate)
            res = str(conjugate)
            self.assertEqual(res,self.conjlist[item])


if __name__ == "__main__":
    unittest.main()