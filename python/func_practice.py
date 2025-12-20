def add(n1,n2):    #n1=in_num1, n2=in_num2
    add=n1+n2
    print("addtion:",add)

def sub(n1,n2):
    sub=n1-n2
    print("Subtraction:",sub)

def mul(n1,n2):
    mul=n1*n2
    print("Multiplication:",mul)

def div(n1,n2):
    div=n1/n2
    print("Division:",div)


in_num1=int(input("Enter 1st integer:"))
in_num2=int(input("Enter 2nd integer:"))
add(in_num1,in_num2)#call function
sub(in_num1,in_num2)
mul(in_num1,in_num2)
div(in_num1,in_num2)
"""
f_num1=float(input("Enter 1nd Float:"))
f_num2=float(input("Enter 2nd float:"))
#f_add=f_num1+f_num2
#print("Addition of float:",f_add)
add(f_num1,f_num2)

s_num1=input("Enter 1nd string:")
s_num2=input("Enter 2nd string:")
#s_add=s_num1+s_num2
#print("Addition of string:",s_add)
add(s_num1,s_num2)
"""
