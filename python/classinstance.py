class Emp:
    def __init__(self,id1,name,salary):
        self.id1=id1
        self.name=name
        self.salary=salary

    def display(self):
        print('Id:',self.id1)
        print('Name:',self.name)
        print('Salary:',self.salary)

class Myclass:
    @staticmethod

    def mymethod(e):
        e.salary+=1000
        e.display()


e=Emp(10,'Rinki',40000)
Myclass.mymethod(e)
        
