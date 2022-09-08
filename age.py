age=int(input("enter the age:"))
if(age>=18):
    print("person is eligible for vote:")
elif(age<18):
    a=18-age
    print("the person is not eligible for vote:",a) 
else:
    print("age will not be in  negative:")
