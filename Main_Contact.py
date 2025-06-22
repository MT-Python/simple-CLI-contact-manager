from file_manager import load_contacts
from add_contact import add_contact
from view_contacts import view_contacts
from search_contact import search_contact
from remove_contact import remove_contact

def main():
    
    contacts = load_contacts()
    print("Welcome to the Contact Book CLI System!")
    print("Loading contacts from contacts.csv... Done!")
    while True:
        print("=========== MENU ===========")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        print("============================")
        choice = input("Enter 1 to 5 Option:-").strip()
        print("============================")
        
        if choice =="1":
            add_contact(contacts)
        elif choice =="2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            remove_contact(contacts)
        elif choice =="5":
            print("Thank you for using the Contact Book CLI System. Goodbye!")
            break
        else:
            print("______Invalid input you enter______ \n")
    
if __name__ == "__main__":
    main()
        