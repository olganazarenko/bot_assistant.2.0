from clases import *


def add_new_contact():
    name = input('Enter name:\n')
    phone = input('Enter phone number:\n')
    if len(phone.split()) > 1:
        print('Enter ONE phone number')
    else:
        if name and phone:
            record_add = Record(name.lower())
            record_add.add_phone(phone)
            addressbook.add_record(record_add)
            print(
                f'A new contact name: {name} phone: {phone}, has been added.')
        else:
            print('Enter correct name and phone.')


def add_new_phone():
    name = input('Enter name:\n')
    phone = input('Enter phone number:\n')
    try:
        record_add_phone = addressbook.data[name]
        record_add_phone.add_phone(phone)
        print(f'A new phone: {phone}, has been added to contact name: {name}.')
    except KeyError:
        print('Enter correct name.')


def change_phone():
    name = input('Enter name:\n')
    phone = input('Enter phone number:\n')
    new_phone = input('Enter new phone number:\n')
    try:
        record_change = addressbook.data[name]
        if record_change.change_phone(old_phone=phone, new_phone=new_phone) is True:
            print(
                f'A contact name: {name} number: {phone}, has been changed to {new_phone}.')
    except KeyError:
        print('Enter correct name.')


def get_contact_number():
    name = input('Enter name:\n')
    try:
        print('name:', addressbook.data[name].name.value, 'phone:',
              list(map(lambda x: x.value, addressbook.data[name].phones)))
    except KeyError:
        print('Enter correct name.')


def quit_func():
    print('Good bye!')
    quit()


def hello_func():
    print("Hello! How can I help you?")


def show_all_func():
    print(f'All contacts:\n{addressbook.data}')


def delete_func():
    name = input('Enter name:\n')
    phone = input('Enter phone number:\n')
    try:
        record_delete = addressbook.data[name]

        if record_delete.delete_phone(phone) is True:
            print(f'Contact name: {name} phone: {phone}, has been deleted.')

    except KeyError:
        print('Enter correct name.')


COMMANDS = {
    'add contact': add_new_contact,
    'add phone': add_new_phone,
    'change': change_phone,
    'phone': get_contact_number,
    'hello': hello_func,
    'show all': show_all_func,
    'good bye': quit_func,
    'close': quit_func,
    'exit': quit_func,
    'delete': delete_func
}
commands = ['add contact', 'add phone', 'change', 'phone',
            'hello', 'show all', 'good bye', 'close', 'exit', 'delete']


def main():

    print('Bot-assistant here...\n("help" - all commands)')

    while True:

        user_input = input('Enter command:\n').lower()
        if user_input == '.':
            break

        if user_input == 'help':
            print(f"All commands: {commands}.")
            continue

        if user_input.split()[0] in COMMANDS:
            COMMANDS[user_input.split()[0]]()

        elif user_input in COMMANDS:
            COMMANDS[user_input]()

        else:
            print(
                f"Sorry, i don't know, what is '{user_input}', please, try again.\nAll commands: {commands}")


if __name__ == "__main__":
    addressbook = AddressBook()
    main()
