import math

class square:
    def area(self,x):
        print('square:%.4f'%x*x)

        
class circle(square):
    def area(self,x):
        print("circle:%.4f"%(math.pi*x*x))
        
c=circle()
c.area(15)





















































