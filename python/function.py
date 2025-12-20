enroll=contact=0
name=address=gender=email=dob=None
enroll=int(input("enter your enrollment number:"))
name=input("enter your name:")
address=input("entre your address:")
contact=int(input("enter your contact number:"))
gender=input("enter your gender:")
email=input("enter email:")

def displaydetails(en,nm,add,con,gen,em):    #en=enroll,nm=name,add=address.....
    print("Enrollment:",enroll)
    print("name:",name)
    print("address:",address)
    print("contact:",contact)
    print("gender:",gender)
    print("email:",email)


displaydetails(enroll,name,address,contact,gender,email)

