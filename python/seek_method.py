file=input("enter your filename:")
try:
    with open(file,'wb+') as f:
        lines=int(input("enter number of lines you want:"))
        for l in range(lines):
            data=input("enter content to write:")
            #d1=data.encode('utf-8')
            f.write(data+"\n")
        print("written")

        print("Current position:",f.tell())
        f.seek(0)
        print("file content:")
        #d2=d2.decode('utf-8')
        print(data.read())
        

except Exception as e:
    print(e)
