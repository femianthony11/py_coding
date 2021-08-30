import math
import classessub
from classessub import Shape
from classessub import Triangle
from classessub import Circle
from classessub import Rectangle
import unittest



class shapeTest(unittest.TestCase):

    def setUp(self):
        #test dict for triangle area and perimeter (a is side 1, b is side 2, and c is side 3.) 
        #In the case where the key is a2b3c1, a=2, b=3, c=1
        #The value of the dictionary is the expected output


        self.tri_area_list = {"a2b2c3":1.984313483298443}
        self.tri_perim_list = {"a2b4c5":11}

        #test dict for circle area and circumference( c is the radius)
        #In the case where the key is c1, c=1
        #The value of the dictionary is the expected output.

        self.circle_area_list = {"c3":28.274333882308138}
        self.circle_circum_list = {"c3": 18.84955592153876}

        #test dict for rectangle area and perimeter ( l is the length and w is the width
        #In the case where the key is l1w2, l=1 and w=2
        #The value of the dictionary is the expected output.

        self.rect_area_list = {"l3w4":12}
        self.rect_perim_list = {"l3w4":14}
        





    def test_triangle(self):
        # Converts list to dictionary 

        def convert(lst):
            res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
            return res_dct

        #splits a list

        def split(word):
            return [char for char in word]

        #for loop to calculate and check triangle area

        for item in self.tri_area_list:
            listt = list(self.tri_area_list)

            listt = split(listt[0])

            dictt = convert(listt)
            
            tri1 = Triangle(dictt)
            print(tri1)

            tri1 = tri1.area()
            print(tri1)
            res = tri1
            self.assertEqual(res,self.tri_area_list[item])
        #for loop to calculate and check circle area






    def test_circle(self):
        # Converts list to dictionary 

        def convert(lst):
            res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
            return res_dct

        #splits a list

        def split(word):
            return [char for char in word]

        for item in self.circle_area_list:
            #reformats list to more easily calculate circle area
            listt = list(self.circle_area_list)

            listt = split(listt[0])

            dictt = convert(listt)
            
            circ1 = Circle(dictt)
            print(circ1)

            circ1 = circ1.area()
            print(circ1)
            res = circ1
            self.assertEqual(res,self.circle_area_list[item])
            
        #for loop to calculate and check circle circumference

        for item in self.circle_circum_list:
            #reformats list to more easily calculate circle circumference
            listt = list(self.circle_circum_list)

            listt = split(listt[0])

            dictt = convert(listt)
            
            circ1 = Circle(dictt)
            print(circ1)

            circ1 = circ1.circumference()
            print(circ1)
            res = circ1
            self.assertEqual(res,self.circle_circum_list[item])

            #for loop to calculate and check rectangle area

    def test_(self):
        # Converts list to dictionary 

        def convert(lst):
            res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
            return res_dct

        #splits a list

        def split(word):
            return [char for char in word]

        for item in self.rect_area_list:
            #reformats list to more easily calculate rectangle area
            listt = list(self.rect_area_list)

            listt = split(listt[0])

            dictt = convert(listt)
            
            rect1 = Rectangle(dictt)
            print(rect1)

            rect1 = rect1.area()
            print(rect1)
            res = rect1
            self.assertEqual(res,self.rect_area_list[item])

        #for loop to calculate and check rectangle perimeter

        for item in self.rect_perim_list:
            listt = list(self.rect_perim_list)

            listt = split(listt[0])

            dictt = convert(listt)
            
            rect1 = Rectangle(dictt)
            print(rect1)

            rect1 = rect1.perimeter()
            print(rect1)
            res = rect1
            self.assertEqual(res,self.rect_perim_list[item])
            





if __name__ == "__main__":
    unittest.main()