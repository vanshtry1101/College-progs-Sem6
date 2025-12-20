
list1=["Amazon","capitalone", 4, 5.9,6,89]

list2=['tech','it',2,3,4,5,6]
#forward indexing - starts with 0
print(list1[5])

#backward indexing
print(list1[-2])

#Operation
#1. addition
addition = list1+list2
print(addition)

#2. replication = repitition
print(list2*2)

#3. slicing
print(list1[0:3:2])
print(list2[::5])
print(list2[-4:-1:1])
print(list2[-1:-3:-1])

#4.update
print(list1)
name=input("enter name to change:")
if(name in list1):
    index1=list1.index(name)
    item=input("enter item to change:")
    list1[index1]=item
    print(list1)
else:
    print("Item not found")

list1=[1,'PPS','LF',4,5]
element=input("enter any element to append:")
if(element.isdigit()):
    element=int(element)
list1.append(element)
print(list1)

list1=[1,'PPS','LF',4,5]
position=int(input("enter position to insert:"))
if(position<=0 or position>=len(list1)+1):
    print("invalid input please enter positive int")
else:
    element=input("enter any element to append:")
    if(element.isdigit()):
        element=int(element)
    list1.insert(position-1,element)
    print(list1)
"""
#sorting
list1=[1,2,3,4,5]
list2=[7,8]

list1.sort(reverse=True)
print(list1)
print(list2)


#extend
list1.extend(list2)
print(list1)

































