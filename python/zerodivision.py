"""
try:
    n1=int(input("enter number 1:"))
    n2=int(input("enter number 2:"))
    assert(n2!=0), "can't divide by zero"
    print("Division:",n1/n2)

except AssertionError as a:
    print(a)

try:
    mark=int(input("enter Marks:"))
    assert(mark>=0 and mark<=100) ,"Invalid input"
    print("marks:",mark)

except AssertionError as a:
    print(a)  
"""

try:
    mark=int(input("enter Marks:"))
    if(mark>=100):
        raise Exception("invalid marks")
except Exception as e:
    print(e)

else:
    print("Mark:",mark)








    
