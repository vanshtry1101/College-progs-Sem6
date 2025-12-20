"""
print("exception handling")
try:
    print(no1)
except NameError:
    print("no such object found.")

print("Blocks of exception")


#input exception
try:
    no=int(input("enter only integer:"))
except ValueError as v:
    print(v)
else:
    print("Number:",no)
finally:
    print("Execption Handling Example.")
"""

list1=[1,3.4,3,4,5]
print(list1)
try:
    index1=int(input("enter index number to find value:"))
    print(list1[index1])
    
except (IndexError, ValueError) as v:
    print("invalid value or index")
    #print("no such index found")
#except ValueError as i:
 #   print(i)
    #print("please enter integer")

print(list1)














