def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
        except KeyError:
            return "Error: Contact not found."
        except TypeError:
            return "Invalid command format."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise ValueError
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError

@input_error
def show_all(contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

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
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()



# Invalid command.
# Enter a command: add
# Give me name and phone please.
# Enter a command: add bob
# Give me name and phone please.
# Enter a command: add bob 05055
# Contact added.
# Enter a command: phone
# Error: Command requires exactly 1 argument: [name]
# Enter a command: all
# Stefan: 388888
# bob: 05055
# Enter a command: gh
# Invalid command.
# Enter a command: g
# Invalid command.
# Enter a command: phone
# Error: Command requires exactly 1 argument: [name]
# Enter a command: phone 4545
# Error: Contact not found.
# Enter a command: phone 05055 
# Error: Contact not found.
# Enter a command: add
# Give me name and phone please.
# Enter a command: add Stefan 333333
# Contact added.
# Enter a command: phone 333333
# Error: Contact not found.
# Enter a command: phone Stefan
# 333333
# Enter a command: