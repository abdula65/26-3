contacts = [
    {'name': 'Geektech', 'phone': '0507052018'},
    {'name': 'Служба спасения', 'phone': '911'},
    {'name': 'Пожарная служба', 'phone': '101'},
]

def create():
    name = input('new name')
    phone = input('name phone')
    contacts.append({"name": name, "phone": phone})
    return contacts

def edit(name):
    new_name = input("New name: ")
    new_phone = input("New phone: ")
    for contact in contacts:
        if name == contact["name"]:
            contact["name"] = new_name
            contact["phone"] = new_phone
    return contacts

def delete():
    name = input('выберите что удалить')
    for contact in contacts:
        if name == contact["name"]:
            a = contacts.index(contact)
            del contacts[a]
    return contacts

while True:
    for i in contacts:
        print(f'{i}')
    dsf = input('выберите команду: ')
    if dsf == '1':
        print(edit('Geektech'))
    elif dsf == '2':
        print(create())
    elif dsf == '3':
        print(delete())