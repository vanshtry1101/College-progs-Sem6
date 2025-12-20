"""
#Keyword arguments 
def display(rno,name,age):
    print(f"rollno:{rno},name:{name},age:{age}")
display(rno=123,age=23,name="rinki")

#default arguments
def display(rno,name,age=0):
    print(f"rollno:{rno},name:{name},age:{age}")
display(1,'rinki')


#practice
def show(ls):
    sum=0
    count=0
    for i in ls:
        #if (type(i)==int or type(i)==float):
            sum+=i
            count+=1
    print(f"sum of {ls}:{sum}")
    print(f"number of element in {ls}:{count}")

list1=input("enter int elements you want in list:").split(',')
list2=[]
for ele in list1:
    if(ele.isdigit()):
        ele=int(ele)
        list2.append(ele)

print(list2)
show(list2)
    
def add(*no):
    sum=0
    for n in no:
        if(type(no)==int or type(no)==float):
            sum+=no
    print("add:",sum)

add(1,2,3,4)


"""
#keyword variable length arguments
def display(**val):
    print(val)
    
display(101=rinki,102=kushwaha)



















