total=0
per=0.0
grade=None
"""
s1=int(input("Enter marks 1:"))
s2=int(input("Enter marks 2:"))
s3=int(input("Enter marks 3:"))

def calculate(s1,s2,s3):
    total=s1+s2+s3
    per=total/3.0
    if per>=70:
        grade="dist"
    else:
        grade="fail"
    return total,per,grade

t=calculate(s1,s2,s3)
print(f"Total marks:{t[0]},percentage:{t[1]},and grade:{t[2]}")
print(t)

rollno=0
def division(rollno):
    if(rollno<=70):
        division='A'
    else:
        division='B'

    return division

rollno=int(input("enter your roll no to check division:"))
div=division(rollno)
print("your Division is:",div)
"""
s1=s2=s3=0
def marks():
    s1=int(input("Enter marks 1:"))
    s2=int(input("Enter marks 2:"))
    s3=int(input("Enter marks 3:"))
    return s1,s2,s3

def cal(s1,s2,s3):
    total=s1+s2+s3
    per=total/3.0
    if per>=70:
        grade="dist"
    elif per>=60:
        grade='first class'
    elif per>=50:
        grade='second class'
    elif per>=40:
        grade='pass'
    else:
        grade='fail'
    return total,per,grade
marks(s1,s2,s3)
t=cal(s1,s2,s3)
print(f"Total marks:{t[0]},percentage:{t[1]},and grade:{t[2]}")
print(t)




















