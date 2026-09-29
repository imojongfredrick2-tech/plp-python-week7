shopping_list = ["milk", "bread", "eggs", "apples"]

print("Shopping List Report")
print(f"Total items: {len(shopping_list)}")

for index, item in enumerate(shopping_list, start=1):
    print(f"{index}. {item}")

print(f"First item: {shopping_list[0]}")
print(f"Last item: {shopping_list[-1]}")
