from abc import ABC,abstractmethod
import math
class Myclass(ABC):
    @abstractmethod
    def cal(self,x):
        pass

class sub1(Myclass):
    def cal(self,x):
        print(x*x)

class sub2(Myclass):
    def cal(self,x):
        print(math.sqrt(x))

class sub3(Myclass):
    def cal(self,x):
        print(x**3)

a1=sub1()
a2=sub2()
a3=sub3()
a1.cal(16)
a2.cal(16)
a3.cal(16)
