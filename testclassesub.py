import math
import classessub
from classessub import Shape
from classessub import Triangle
from classessub import Circle
from classessub import Rectangle
import unittest



class shapeTest(unittest.TestCase):

    def setUp(self):


        self.triarealist = {"a2b2c3":1.984313483298443}
        self.triperimlist = {"a2b4c5":11}
        self.circarealist = {"c3":28.274333882308138}
        self.circcircumlist = {"c3": 18.84955592153876}
        self.rectarealist = {"l3w4":12}
        self.rectperimlist = {"l3w4":14}

        self.oplist = {"+":"4+6i","-":"-2-2i","*":"-5+10i"}



    def test_fact(self):

        def Convert(lst):
            res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
            return res_dct
        def split(word):
            return [char for char in word]



        for item in self.triarealist:
            listt = list(self.triarealist)

            listt = split(listt[0])

            dictt = Convert(listt)
            
            tri1 = Triangle(dictt)
            print(tri1)

            tri1 = tri1.area()
            print(tri1)
            res = tri1
            self.assertEqual(res,self.triarealist[item])

        for item in self.circarealist:
            listt = list(self.circarealist)

            listt = split(listt[0])

            dictt = Convert(listt)
            
            circ1 = Circle(dictt)
            print(circ1)

            circ1 = circ1.area()
            print(circ1)
            res = circ1
            self.assertEqual(res,self.circarealist[item])
            

        for item in self.circcircumlist:
            listt = list(self.circcircumlist)

            listt = split(listt[0])

            dictt = Convert(listt)
            
            circ1 = Circle(dictt)
            print(circ1)

            circ1 = circ1.circumference()
            print(circ1)
            res = circ1
            self.assertEqual(res,self.circcircumlist[item])

        for item in self.rectarealist:
            listt = list(self.rectarealist)

            listt = split(listt[0])

            dictt = Convert(listt)
            
            rect1 = Rectangle(dictt)
            print(rect1)

            rect1 = rect1.area()
            print(rect1)
            res = rect1
            self.assertEqual(res,self.rectarealist[item])

        for item in self.rectperimlist:
            listt = list(self.rectperimlist)

            listt = split(listt[0])

            dictt = Convert(listt)
            
            rect1 = Rectangle(dictt)
            print(rect1)

            rect1 = rect1.perimeter()
            print(rect1)
            res = rect1
            self.assertEqual(res,self.rectperimlist[item])
            





if __name__ == "__main__":
    unittest.main()