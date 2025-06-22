from file_manager import save_contacts

def remove_contact(contacts):
    phone = input("Enter the phone number of the contact to delete: ").strip()
    for c in contacts:
        if c["phone"] == phone:
            confirm = input(f"Are you sure you want to delete contact number {phone}? (y/n): ").lower()
            if confirm == 'y':
                contacts.remove(c)
                save_contacts(contacts)
                print("Contact deleted successfully!")
                return
            else:
                print("delete canceled.")
                return
    print("contact not found in txt file")