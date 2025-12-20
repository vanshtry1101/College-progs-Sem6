try:
    enroll=int(input("enter your enroll:"))
    assert (enroll>70) ,"not eligible for B"
    print("your division will be B")

except (AssertionError,ValueError) as a:
    print(a)
except Exception as e:
    print(e)
