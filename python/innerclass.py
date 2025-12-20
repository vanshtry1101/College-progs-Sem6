class person:
    def __init__(self):
        self.name='Rinki'
        self.db=self.Dob()

    def display(self):
            print('Name:',self.name)
    class Dob:
        def __init__(self):
            self.dd=10
            self.mm=5
            self.yy=1999
        def display(self):
            print('DOB={}/{}/{}'.format(self.dd,self.mm,self.yy))
                
p=person()
p.display()

x=p.db
x.display()
