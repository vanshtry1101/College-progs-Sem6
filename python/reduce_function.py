#product of all the elements of list 
from functools import reduce
list1=list(range(1,6))
print(list1)
product=reduce(lambda n1,n2: n1*n2,list1)
print(product)


