def load_contacts():
    contacts=[]
    try:
        with open ("contacts.txt","r")as file:
            for line in file:
                name,phone,email,address = line.strip().split("|")
                contacts.append(
                    {
                        "name":name,
                        "phone":phone,
                        "email":email,
                        "address":address
                    }
                )
    except FileNotFoundError:
        print("contacts.txt not found.Please Create contact.txt file")
    return contacts

def save_contacts(contacts):
    with open ("contact.txt","w") as file:
        for c in contacts:
            line=f"{c['name']} | {c['phone']} | {c['email']} | {c['address']} \n"
            file.write(line)
    