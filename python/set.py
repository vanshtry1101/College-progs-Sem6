#union()
set1={1,2,3,4,5,6,7,8,9,10,11,12,13}
set2={5,6,7,14}

#set3=set1 | set2
set3=set1.union(set2)
print(f"Union of set: {set3}")

#Intersection()
#set3= set1 & set2
set3=set1.intersection(set2)
print(f"Intersection of {set1} and {set2} is: {set3}")

#Difference()
set3=set1-set2
print(f"Difference of {set1} and {set2} : {set3}")

#Symetric Difference()
set3=set1 ^ set2
print("Symetric Difference:",set3)

#add()
element=int(input("enter element to add:"))
if(element in set1):
    print("element already exist:")
else:
    set1.add(element)
print(set1)


#remove()
element=int(input("enter element to remove:"))
if(element not in set1):
    print("element doesn't exist")
else:
    set1.remove(element)
    print(set1)

#pop()
set1.pop()
print(set1)
"""

#Issubset()
print(f"Is set2:{set2} subset of set1:{set1}: {set2.issubset(set1)}")

#Isuperset()
print(f"Is set1:{set1} subset of set2:{set2}: {set1.issuperset(set2)}")







