price = int(input("Enter the price of an item: "))
if price > 1000:
    price *= .90
elif price > 500:
    price *= .95
print(f"The final price after discount is: Rs. {price}")