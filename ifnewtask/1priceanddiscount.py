price = float(input("Enter the price of the item: "))

if price > 1000:
    discount = price * 0.10
    final_price = price - discount
elif price > 500:
    discount = price * 0.05
    final_price = price - discount
else:
    final_price = price

print("The final price is:", final_price)
