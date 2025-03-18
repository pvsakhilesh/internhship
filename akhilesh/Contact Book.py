def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")
    contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
    contacts.append(contact)
    print(f"Contact for {name} added successfully.")
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]
    if found_contacts:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    else:
        print("No matching contacts found.")
def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Updating contact for {name}:")
            contact['name'] = input(f"Enter new name (current: {contact['name']}): ") or contact['name']
            contact['phone'] = input(f"Enter new phone (current: {contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Enter new email (current: {contact['email']}): ") or contact['email']
            contact['address'] = input(f"Enter new address (current: {contact['address']}): ") or contact['address']
            print(f"Contact for {contact['name']} updated successfully.")
            return
    print(f"No contact found with the name {name}.")
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact for {name} deleted successfully.")
            return
    print(f"No contact found with the name {name}.")
def main():
    contacts = []  # List to store contacts
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option.")
if __name__ == "__main__":
    main()