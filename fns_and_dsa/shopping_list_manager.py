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
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Prompt for and add an item
          name = input("Enter the item to add: ")
          shopping_list.append(name)
        elif choice == 2:
            # Prompt for and remove an item
          name = input("Enter the item to remove: ")
          if name in shopping_list:
              shopping_list.remove(name)
          else:
              print("The item does not exist")

        elif choice == 3:
            # Display the shopping list
          print(shopping_list)
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
          
