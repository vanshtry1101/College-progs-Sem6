class father:
    def height(self):
        print("height:6 feet")

class mother:
    def color(self):
        print("color is brown")

class child(father,mother):
    pass

c=child()

c.height()
c.color()
