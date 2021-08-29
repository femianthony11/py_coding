import math
from math import sqrt
class Shape:
    

    def __init__(self,dim):
        self.dim = dim

    def area(self):
        pass
        




class Triangle(Shape):
    def __init__(self,dim):
        self.dim = dim
        #THIS IS THE BASE
        self.a = int(dim['a'])
        #THIS IS THE HEIGHT
        self.b = int(dim['b'])

        self.c = int(dim['c'])

    def perimeter(self):
        perim = self.a+self.b+self.c
        return perim

    def area(self):
        s1 = (self.a+self.b+self.c)/2
        area = sqrt(s1*((s1-self.a)*(s1-self.b)*(s1-self.c)))
        return area
    
    def __str__(self):
        return (f"Triangle Dimensions ={self.dim}")


class Circle(Shape):
    def __init__(self,dim):
        self.dim = dim
        self.rad = int(dim['c'])

    def area(self):
        area = (self.rad**2)*math.pi
        return area

    def circumference(self):
        circumference = 2*(math.pi)*self.rad
        return circumference

    def __str__(self):
        return (f"Circle ={self.dim}")



class Rectangle(Shape):

    def __init__(self,dim):
        self.dim = dim
        self.length = int(dim['l'])
        self.width = int(dim['w'])
    
    def area(self):
        area = self.length*self.width
        return area

    def perimeter(self):
        perimeter = 2*(self.length+self.width)
        return perimeter


    def __str__(self):
        return (f"Rect Dimensions ={self.dim}")




def main():
    rect_dim = {"l":2,"w":3}
    triangle_dim = {"a":1,"b":2,"c":3}
    circle_dim = {"c":4}



    tri = Triangle(triangle_dim)
    print(tri)

    tri_area = tri.area()
    print(f"Triangle Area = {tri_area}")

    tri_perim = tri.perimeter()
    print(f"Triangle Perimeter = {tri_perim}")


    Circ = Circle(circle_dim)
    print(Circ)

    Circ_area = Circ.area()
    print(f"Circle Area = {Circ_area}")

    Circ_circum = Circ.circumference()
    print(f"Circumference = {Circ_circum}")

    rect = Rectangle(rect_dim)
    print(rect)


    rect_area = rect.area()
    print(f"Rect Area = {rect_area}")


    rect_perim = rect.perimeter()
    print(f"Rect Perim = {rect_perim}")



if __name__ == "__main__":
    main()