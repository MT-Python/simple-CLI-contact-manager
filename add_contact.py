from file_manager import save_contacts

def add_contact(contacts):
    print("===== All Contacts =====")
    name = input("Name:").strip()
    phone = input("Phone Number:").strip()
    email = input("Email Address:").strip()
    address = input("Address:").strip()
    
    if not phone.isdigit():
        print("Your Phone number must be Digits only")
        return
    
    for c in contacts:
        if c["phone"] ==phone:
            print("Phone number already exists for another contact.")
            return
        
    for c in contacts:
        if c["email"] == email:
            print("Email  already exists for another contact.")
            return
        
    contacts.append(
        {
            "name":name,
            "phone":phone,
            "email":email,
            "address":address
        }
    )
    save_contacts(contacts)
    print("your Contact saved")