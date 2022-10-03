n=int(input("enter the no of lower:"))
m=int(input("enter the no of day old loans:"))
regular_price=185
amount_of_new_lower=(n*regular_price)
amount_of_day_old_lower=(m*regular_price*6)/10
total_amount=amount_of_new_lower+amount_of_day_old_lower
print("regular price:",regular_price)
print("amount of new lower:",amount_of_new_lower)
print("amount of day old lower:",amount_of_day_old_lower)
print("total amount:",total_amount)
