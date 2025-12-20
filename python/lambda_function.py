"""
square=lambda n1:n1**2
num1=int(input("enter number to print square:"))
print(f"square of {num1}:{square(num1)}")


cube=lambda no1:no1**3
num2=int(input("enter number to print cube:"))
print(cube(num2))

#product of two numbers:
product=lambda n1,n2:n1*n2
num1=int(input("enter number1:"))
num2=int(input("enter number2:"))
print(f"product of two numbers:{product(num1,num2)}")


#swap two variables:
swap=lambda n1,n2:(n2,n1)
num1=int(input("enter number1:"))
num2=int(input("enter number2:"))
print(f"swap of two numbers:{swap(num1,num2)}")
"""

#functions of lambda
#1.Filter()

#list1=[1,2,3,4,5,"abc",True]
"""
list1=[]
num=int(input("enter no. of elements you wants:"))
for n in range(1,num+1):
    list1.append(n)
print("list of elements:",list1)

odd=filter(lambda no:no%2!=0,list1)
print("odd:",tuple(odd))



list1=[]
n=int(input("enter number of elements you want:"))
for i in range(n+1):
    ele=input("enter first string:")
    list.append()
print(list1)


str1=input("enter a string:")
vowels=filter(lambda char:char in "aeiouAEIOU",str1)
print(f"list of vowels in {str1}:{list(vowels)}")



#map creates new list of elements and filter use to filter the elements from the list
#filter=layoff map=update
list1=[1,2,3,4,5,6]
print(list1)
cube=map(lambda elem:elem**3,list1)
print(tuple(cube))
"""


list1=[5000,2000,3000]
print(list1)
salary=map(lambda ele:ele+ele*0.10,list1)
print(list(salary))

#product %5 decreament
product=map(lambda ele:ele-ele*0.5,list1)
print(list(salary))
















































