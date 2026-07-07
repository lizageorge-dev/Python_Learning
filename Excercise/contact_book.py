# Contact Book Program

# Function to add a new contact
def add_contact(contacts):
    # Get contact name from the user
    name = input("Enter contact name: ").strip()

    # Check if the contact already exists
    if name in contacts:
        print("Contact already exists! Duplicate names are not allowed.")
        return

    # Get phone number from the user
    phone = input("Enter phone number: ").strip()

    # Validate phone number (digits only)
    if not phone.isdigit():
        print("Invalid phone number! Please enter digits only.")
        return

    # Add contact to the dictionary
    contacts[name] = phone
    print("Contact added successfully!")


# Function to display all contacts
def view_contacts(contacts):
    # Check if the dictionary is empty
    if not contacts:
        print("Contact list is empty.")
        return

    print("\n--- Contact List ---")

    # Display contacts in alphabetical order
    for name in sorted(contacts):
        print(f"Name: {name}, Phone: {contacts[name]}")


# Function to search for a contact
def search_contact(contacts):
    # Ask user for a name or partial name
    search_name = input("Enter name to search: ").strip().lower()

    found = False

    # Loop through all contacts
    for name, phone in contacts.items():
        # Check for partial match
        if search_name in name.lower():
            print(f"Name: {name}, Phone: {phone}")
            found = True

    # Display message if no match is found
    if not found:
        print("No matching contact found.")


# Function to delete a contact
def delete_contact(contacts):
    # Ask user for the contact name
    name = input("Enter contact name to delete: ").strip()

    # Check if contact exists
    if name in contacts:
        # Remove contact from dictionary
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


# Function to display the menu
def display_menu():
    print("\n===== Contact Book Menu =====")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


# Main function that controls the program
def main():
    # Dictionary to store contacts
    # Key = Contact Name
    # Value = Phone Number
    contacts = {}

    # Keep showing the menu until the user exits
    while True:
        display_menu()

        try:
            # Get menu choice from the user
            choice = int(input("Enter your choice (1-5): "))

            # Call appropriate function based on choice
            if choice == 1:
                add_contact(contacts)

            elif choice == 2:
                view_contacts(contacts)

            elif choice == 3:
                search_contact(contacts)

            elif choice == 4:
                delete_contact(contacts)

            elif choice == 5:
                print("Thank you for using Contact Book. Goodbye!")
                break

            # Handle invalid menu choices
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")

        # Handle non-numeric input
        except ValueError:
            print("Invalid input! Please enter a valid number.")

        # Handle any unexpected errors
        except Exception as e:
            print(f"An error occurred: {e}")


# Start the program
main()