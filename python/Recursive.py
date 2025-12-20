def fact(num):
    if(num<0):
        return "not possible"
    elif(num==0 or num==1):
        return 1
    else:
        return num*fact(num-1)

n1=int(input("Enter number to find factorial:"))
ans=fact(n1)
print(f" Factorial of {n1} is {ans}")
