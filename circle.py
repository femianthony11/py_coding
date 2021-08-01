
class  Circle():

    def __init__(self,r):
        self.radius = r

    def area(self):
            return self.radius**2*3.14
        
    def circumference(self):
        return 2*self.radius*3.14
Circle1 = Circle(5)
print("Area: " + str(Circle1.area()))
print("Circumference: " + str(Circle1.circumference()))
