class Myclass:
    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif(a!=None and b!=None):
            print(a+b)
        else:
            print("enter two ags")

m=Myclass()
m.sum(10,15,20)
