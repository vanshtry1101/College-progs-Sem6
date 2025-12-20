#dictionary

dictionary={'technical':60,"sales":30,'marketing':200}
print(dictionary)

#print using key
print(dictionary['sales'])

debt={0:'',1:'',2:''}
print(debt)
#key should be unique

#if we want to put multiple values in one key, then use tuple or list 
dic1={102:[20,30,20],103:''}
print(dic1)

#operation

#updation
debt[0]='abc'
print(debt)

#deletion
#abs1={ans:'sds'}
#print(abs1)

#del abs1
#print(abs1)

#len()
print("Total number of items:",len(debt))

#methods
#1. keys()
print(debt.keys())


'''
#2.values()
print(debt.values())

#3.items()
print(debt.items())

#4. clear()
#debt.clear()
#print(debt)

#5. copy()
emp={}
print(debt)
print(emp)
#emp=debt.copy()
#emp.copy(debt) not working
#emp=debt
print(debt)
print(emp)
'''
#







