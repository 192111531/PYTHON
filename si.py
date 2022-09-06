def simple_interest(p_amount,time,rate):
   simple_interest=(p_amount*time*rate)/100
   return simple_interest
p_amount=int(input("enter the principle_amount:"))
rate=int(input("enter the rate:"))
time=int(input("enter the time:"))
si=simple_interest(p_amount,time,rate)
print("the simple interest is:",si)
    
