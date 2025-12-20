'''
name=input("Enter Number:")
total=len(name)
rev=''
for i in range(total-1,-1,-1):
    rev+=name[i]
print(f"reverse string {name} is {rev}")
'''
name=input("Enter Number:")
total=len(name)+1
rev=''
for i in range(-1,-total,-1):
    rev+=name[i]
print(f"reverse string {name} is {rev}")

