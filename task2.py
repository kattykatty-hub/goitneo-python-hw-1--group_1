def parse_input(user_input):
    cmd, *args = user_input.split(maxsplit=2)
    cmd = cmd.strip().lower()
    return cmd, args


def add_or_change_contact(args, contacts):
    if len(args) != 2:
        return "Please input the command in the format: add [name] [phone]"

    name, phone = args
    contacts[name] = phone
    return "Contact added/changed."


def print_phone_by_name(args, contacts):
    if not args:
        return "Please provide a name to search for."
    
    name = args[0]
    if name not in contacts:
        return f"No contact found for {name}."
    
    phone = contacts[name]
    return f"{name}: {phone}"


def print_all_contacts(contacts):
    if not contacts:
        return "No contacts available."
    
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add" or command == "change":
            print(add_or_change_contact(args, contacts))
        elif command == "phone":
            print(print_phone_by_name(args, contacts))
        elif command == "all":
            print(print_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
