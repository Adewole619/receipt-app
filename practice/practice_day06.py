items = []

count = int(input("How many items? "))

for i in range(count):
    item = input("Enter item: ")
    items.append(item)

print(items)
print(len(items))