def arithmetic(operation,*num):
    if(operation=='add'):
        sum=0
        for i in num:
            if(type(i)==int or type(i)==float):
                sum+=i
        print("addition:",sum)
    elif(operation=='*'):
        mul=1
        for i in num:
            if(type(i)==int or type(i)==float):
                mul*=i
        print("multiplication:",mul)
    elif(operation=='-'):
        mul=0
        for i in num:
            if(type(i)==int or type(i)==float):
                mul-=i
        print("multiplication:",mul)
arithmetic("add",1,2,3,4)
arithmetic("*",2.2,2.2)
