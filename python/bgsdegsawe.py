from abc import ABC,abstractmethod
import math

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter():
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*(self.radius)**2

    def perimeter(self):
        return 2*math.pi*self.radius

class rectangle(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*self.width+self.height

c=circle(5)
r=rectangle(4,6)

print(c.area())
print(r.area())










