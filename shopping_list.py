# Start with an empty shopping list
items = []

# Keep showing the menu until the user chooses done
while True:
    choice = input("add / remove / show / done: ").lower()

    # Add an item
    if choice == "add":
        item = input("Add what? ")
        items.append(item)
        print("Item added.")

    # Remove an item
    elif choice == "remove":
        item = input("Remove what? ")

        if item in items:
            items.remove(item)
            print("Item removed.")
        else:
            print("That item is not on your list.")

    # Show all items
    elif choice == "show":
        if len(items) == 0:
            print("Your shopping list is empty.")
        else:
            print("Shopping list:")
            for item in items:
                print(item)

    # Stop the program
    elif choice == "done":
        print("Shopping list finished.")
        break

    # Handle an invalid choice
    else:
        print("Invalid choice. Please choose add, remove, show, or done.")