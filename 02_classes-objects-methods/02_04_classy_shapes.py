# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"{self.length},{self.width}"

    def RectanglePerimeter(self):
        perimeter = 2 * (self.length + self.width)
        print(perimeter)

class Circle:
    def __init__(self, circleradius):
        self.circleradius = circleradius

    def circumference(self):
        perimter = 2* 3.14 * self.circleradius
        print(perimter)
       

    def __str__(self):
        return f"{self.circleradius}"    

rectangle1 = Rectangle(3,4)
print(rectangle1)
rectangle1.RectanglePerimeter()
circle1 = Circle(2)
print(circle1)
circle1.circumference()




    
