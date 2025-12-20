import sys
from arithmetic import *

while(True):
    print("1.Addition") 
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division") 
    print("5.Exit")
    c=int(input("Enter your choice:"))
    num1=int(input("enter first number:"))
    num2=int(input("enter second number:"))

    if(c==1):
        print("addition:",add(num1,num2))
    elif(c==2):
        print("Subtraction:",sub(num1,num2))
    elif(c==3):
        print("Multiplication:",mul(num1,num2))
    elif(c==4):
        print("Division:",div(num1,num2))
    elif(c==5):
        sys.exit()
