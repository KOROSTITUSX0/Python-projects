#Polymorphism = Greek word that means to "have many forms or faces"
#              Poly =  Many
#              Morphe = Form

#               TWO WAYS TO ACHIEVE POLYMORPHISM
#               1. Inheritance = An object could be treated of the same type as a parent class
#               2."Duck typing" = Object must have necessary attribute/methods

from abc import abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return f"Area of the circle is {3.14 * self.radius ** 2}"
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return f"Area of the square is {self.side ** 2}"
class Triangle(Shape):
    def __init__(self,base, height):
        self.base = base
        self.height = height
    def area(self):
        return f"Area of the Triangle {self.base * self.height * 0.5}"
class Pizza(Circle):
    def __init__(self, tapping, radius):
        super().__init__(radius)
        self.tapping = tapping
shapes = [Circle(4), Square(3),Triangle(2, 6),Pizza("Pepperoni", 15) ]
for shape in shapes:
    print(f"{shape.area()}cm²")