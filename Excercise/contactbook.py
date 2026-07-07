exit=False
contact_info={}
def add_contact():
    name=input("Enter name: ")
    phone=input("Enter phone number: ")
    contact_info[name]=phone
    print("Contact added successfully!")
def view_contacts():
    if not contact_info:
        print("Contact list is empty.")
        return
    print("\n--- Contact List ---")
    for name in sorted(contact_info):
        print(f"Name: {name}, Phone: {contact_info[name]}")
def search_contact():
    search_name = input("Enter name to search: ").strip().lower()
    found = False
    for name, phone in contact_info.items():
        if search_name in name.lower():
            print(f"Name: {name}, Phone: {phone}")
            found = True
    if not found:
        print("No matching contact found.")
def delete_contact():
    name = input("Enter contact name to delete: ").strip()
    if name in contact_info:
        del contact_info[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def display_menu():
    print("\n===== Contact Book Menu =====")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def main():
    exit = False
    while exit==False:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                add_contact()
            elif choice == 2:
                view_contacts()
            elif choice == 3:
                search_contact()
            elif choice == 4:
                delete_contact()
            elif choice == 5:
                print("Thank you for using Contact Book. Goodbye!")
                exit = True
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

main()
    main()