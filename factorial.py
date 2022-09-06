number=int(input("enter the number:"))
factorial=1
if(number<0):
    print("factorial does not exist:")
elif(number==0):
    print("factorial of 0 is 1:")
else:
    for i in range(1,number+1):
        factorial=factorial*i
    print("the factorial of",number,"is",factorial)
    
