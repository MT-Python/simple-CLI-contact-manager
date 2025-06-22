def view_contacts(contacts):
    if not contacts:
        print("there have no contacts")
        return
    
    print("\n=========== ALL CONTACTS LIST ===========\n")
    for i , c in enumerate(contacts,1):
        
        print(f"{i}. {c['name']}, {c['phone']}, {c['email']}, {c['address']} \n")
        print("============================")