contacts = []


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email (optional): ").strip()

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })
    print("Contact added.\n")


def view_contacts():
    if not contacts:
        print("No contacts available.\n")
        return
    print("\n--- Contact List ---")
    for c in contacts:
        print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
    print()


def search_contact():
    name = input("Enter name to search: ").strip()
    found = False
    for c in contacts:
        if c['name'].lower() == name.lower():
            print(f"Found -> Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}\n")
            found = True
    if not found:
        print("No contact found.\n")


def delete_contact():
    name = input("Enter name to delete: ").strip()
    for c in contacts:
        if c['name'].lower() == name.lower():
            contacts.remove(c)
            print("Contact deleted.\n")
            return
    print("Contact not found.\n")


def menu():
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    menu()
