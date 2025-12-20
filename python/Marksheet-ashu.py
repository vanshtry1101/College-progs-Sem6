class student(object):
    no=0
    
    def __init__(self,sname=None, m1=0,m2=0,m3=0):
        student_no=student_no+1
        self.sname=sname
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.total=0
        self.percentage=0.0
        self.grade=""
        self.caltotal()
        self.calpercentage()
        self.calgrade()
    @staticmethod
    def objects():
        print(f"Student ID:{student_no}") 

    def show(self):
        student.objects()
        print(f"Student Name:{self.sname}")
        print(f"Mark1:{self.m1}")
        print(f"Mark2:{self.m2}")
        print(f"Mark3:{self.m3}")
        print(f"Total:{self.total}")
        print(f"percentage:{self.percentage}")
        print(f"grade:{self.grade}")
        print("-----------------------------------------")
        
    def caltotal(self):
        self.total=self.m1+self.m3+self.m3

    def calpercentage(self):
        self.percentage=self.total/3.0

    def calgrade(self):
        if self.percentage >= 90:
            self.grade='O'
        elif self.percentage >= 80:
            self.grade='A'
        elif self.percentage >= 70:
            self.grade='B'
        elif self.percentage >= 60:
            self.grade='C'
        elif self.percentage >= 50:
            self.grade='D'
        else:
            self.grade='F'
    def update_mark(self):
        self.caltotal()
        self.calpercentage()
        self.calgrade()
                
    def get_name(self):
        return self.sname

    def set_name(self,name):
       self.name=name

    def get_m1(self):
        return self.m1

    def set_m1(self,m1):
       self.m1=m1
       self.update_mark()

    def get_m2(self):
        return self.m2

    def set_m1(self,m2):
       self.m2=m2
       self.update_mark()

    def get_m3(self):
        return self.m3

    def set_m1(self,m3):
       self.m3=m3
       self.update_mark()
        
if __name__=="__main__":
    
    s1=student('Rinki',80,80,79)
    s1.show()
    
    s1.set_name("Mohit")
    s1.set_m1(70)
    s1.set_m2(60)
    s1.set_m3(79)
    s1.show()
    









