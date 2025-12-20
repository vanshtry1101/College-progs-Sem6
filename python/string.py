#Funtions

#basic- conceti.
str1="rinki"
str2="kushwaha"
print(str1+' '+str2)

#membership operator
#in and not in 
print('d' in str1)
print('d' in 'RDBMS')
print('d' not in 'RDBMS')
print('D' in 'RDBMS')

#slice- small part of string=substring
print(str2[4:7])
print(str2[::-1])
print(str2[::])
print(str2[2:6])
print(str2[7:1:-1])

#len() fucntion
print(len(str2))

#methods
str3='celebro'

#capitalize()
print(str3.capitalize())

#lower()
print(f"Lowercase of string:{str3.lower()}")

#upper()
print(f"uppercasr of string:{str3.upper()}")

#islower()
print(f"check string is in lowercase or not:{str3.islower()}")

#isupper()
print(f"check string is in uppercase or not:{str3.isupper()}")

#swapcase()
print(str3.swapcase())

str5="rinki23"
#isalnum()
print(f"is {str5} alnum?: {str5.isalnum()}")

#isalpha()
print(f"is {str5} alphabets:{str5.isalpha()}")


#isspace()
print(f"is {str5} space: {str5.isspace()}")


#isdigit()
print(f"is {str5} number: {str5.isdigit()}")

#startswith()
str6="This is not number"
#check=input("Enter String:")
#print(f" '{str6}' start with '{check}' : {str6.startswith(check)}")

#endswith()
check=input("Enter String:")
print(f" '{str6}' ends with '{check}' : {str6.endswith(check)}")

#find()
check=input("Enter character to find:")
print(f" '{str6}' is in {str6}: {str6.find(check)}")

#index()
str7=" There is no index in this file "
#check=input("Enter character is to find index:")
#print(str7.index(check))

#Count()
check=input("enter string to count:")
print(str7.count(check,0,15))

"""

































