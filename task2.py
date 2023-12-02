def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    # Спосіб 1
    # if len(args) != 2:
    #     return "Please input commmand for add_contacts in next patter\nadd [ім'я] [номер телефону]"
    # name, phone = args

    # Спосіб 2
    try:
        name, phone = args
    except ValueError:
        return "No response"

    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts: dict):
    name, phone = args
    if name not in contacts:
        return "NO person with such contact"

    contacts[name] = phone
    return "Contact added."


def print_phone_by_name(args, contacts):
    name = args[0]
    if name not in contacts:
        return "we cant find such user in our contacts"
    phone = contacts[name]
    return f"{name=} {phone=}"


def print_all_contacts(args, contacts):
    return "\n".join(
        f"{name=} {phone=}" for name, phone in contacts.items()
    )


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(print_phone_by_name(args, contacts))
        elif command == "all":
            print(print_all_contacts(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
