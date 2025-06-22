def search_contact(contacts):
    term = input("Enter search term (name/email/phone): ").lower()
    found = False
    for c in contacts:
        if term in c["name"].lower() or term in c["phone"] or term in c["email"].lower():
            print("Search Result:")
            print(f"\n name:{c['name']}, \n Phone: {c['phone']}, \n email: {c['email']}, \n Address: {c['address']}\n")
            print("============================ \n")
            found = True
        if not found:
            print("++++No Contact Found++++")