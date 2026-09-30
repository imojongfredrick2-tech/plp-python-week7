# Create a shopping list
items = ["bread", "milk", "chicken", "tomatoes", "toothpaste"]

print("Shopping List Report")
print("---------------------")

# Number the items
number = 1

for item in items:
    print(f"{number}. {item}")
    number += 1

# Count items with more than 4 characters
count = 0

for item in items:
    if len(item) > 4:
        count += 1

print()
print("Items with more than 4 characters:", count)

# Find the longest item
longest = ""

for item in items:
    if len(item) > len(longest):
        longest = item

print("Longest item:", longest)