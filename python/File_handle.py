"""
file1=open("hello.txt","w")
file1.write("this is write method")
file1.writelines(["Hello\n","\tWorld"])
print("write successfully")
file1.close()


file2=open("hello.txt")
print(file2.readline())
print(file2.readlines())
file2.close


file3=input("enter filename to write:")
f3=open(file3,"w")

list1=[]
line=int(input("enter number of lines you want to write:"))
for i in range(line):
    data=input("enter lines to write:")
    list1.append(data+"\n")
f3.writelines(list1)


filename=input("enter file name to read:")
try:
    f1=open(filename)
    print(f1.read())
    f2.close()
except Exception as e:
    print(e)


filename=input("enter file name:")
with open(filename,'a') as f1:
    lines=int(input("enter number of lines you want:"))
    for l in range(lines):
        data=input("enter content to write:")
        f1.write(data+"\n")
    print("successfully created")


list1=[]
filename=input("enter file name:")
with open(filename,'a') as f1:
    lines=int(input("enter number of lines you want:"))
    for l in range(lines):
        data=input("enter content to write:")
        list1.append(data)
    f1.writelines(data+"\n")
    print("successfully created")



file1=input("enter name of file:")
with open(file1,'a+') as file:                              #Append
    lines=int(input("enter number of lines you want:"))
    for i in range(lines):
        data=input("Enter content to write:")
        file.write(data+"\n")
    print("Written Successfully")
    print("----------------------------------------")
    print("current poisition:",file.tell())

    file.seek(0)
    print("file data:")
    print(file.read())



file1=input("enter name of file:")
with open(file1,'r+') as file:                              #Read
    lines=int(input("enter number of lines you want:"))
    for i in range(lines):
        data=input("Enter content to write:")
        file.write(data+"\n")
    print("Written Successfully")
    print("----------------------------------------")
    print("current poisition:",file.tell())

    file.seek(0)
    print("file data:")
    print(file.read())

"""



file1=input("enter name of file:")
try:
    with open(file1,'r+') as file:
        file.seek(0)
        print("file data:")
        print(file.read())              #Read
        lines=int(input("enter number of lines you want:"))
        for i in range(lines):
            data=input("Enter content to write:")
            file.write(data+"\n")
        print("Written Successfully")
        print("----------------------------------------")
        print("current poisition:",file.tell())

except FileNotFoundError as f:
    print(f)




























    
