# number1 = int(input("First number: "))
# number2 = int(input("Second number: "))

# print("Addition:", number1 + number2)
# print("Subtraction:", number1 - number2)
# print("Multiplication:", number1 * number2)
# print("Division:", number1 / number2)
# print("Remainder:", number1 % number2)

# print()
# print()

total = 100

total += 50
print(total)

total -= 20
print(total)

total *= 2
print(total)

total /= 5
print(total)

print()
print()

store = input("Enter your store name: ")
item = input("Enter item: ")
price = int(input("Enter price: "))
quantity = int(input("Enter quantity: "))
subtotal = price * quantity

print("========================")
print("         RECEIPT")
print("========================")
print()
print()
print(f"store: {store}")
print(f"Item: {item}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")

print()
print()
print(f"subtotal: {subtotal:.2f}")

print()
print()
print("Thank you for shopping!")
