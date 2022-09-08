start=int(input("enter the number:"))
stop=int(input("enter the number:"))
for n in range(start,stop+1):
    sum=0
    for i in range(1,n):
        if(n%i==0):
         sum+=i
    if(n==sum):
       print("numbers:",n)
