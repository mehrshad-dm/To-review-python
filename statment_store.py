price = int(input("Enter your purchase amount:"))

if price > 50000:
    discount = price * 0.2
elif  price > 20000:
    discount = price * 0.1
else:
    discount = 0

final_price = price - discount
print(f"Final price is: {int(final_price)}")