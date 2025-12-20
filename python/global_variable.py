a=45
def show():
    global a
    print("value of a before changes inside function:",a)
    a=55
    print(" value of a after changes:",a)
show()
print("Outside function:",a)
