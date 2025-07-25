def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item_add = input("Enter the item to add: ")
            shopping_list.append(item_add)
            pass
        elif choice == '2':
            item_deleted = input("Enter the item to delete: ")
            if item_deleted in shopping_list:
                shopping_list.remove(item_deleted)
            else:
                print("Item not found in the shopping list")
            pass
        elif choice == '3':
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()