phone_book = {}


def add_or_change_phone(strip):
    words = strip.split(' ')
    if len(words) > 3:
        raise ValueError
    phone_book[words[1]] = words[2]


def get_phone(strip):
    words = strip.split(' ')
    result = phone_book.get(words[1], 1)
    if result == 1:
        raise KeyError
    else:
        return result


def input_error(func):
    def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except KeyError:
                print('No phone for this contact, try again')
                inner(*args, **kwargs)
            except ValueError:
                print('Enter correct command')
                inner(*args, **kwargs)
            except IndexError:
                print('Enter correct username or phone')
                inner(*args, **kwargs)
    return inner


@input_error
def main():
    while True:
        user_input = input('Enter your command: ')
        command = user_input.lower()
        if command.startswith('hello'):
            print('How can I help you?')
        elif command.startswith('add') or command.startswith('change'):
            add_or_change_phone(command)
            print('Phone saved')
        elif command.startswith('phone'):
            get_phone_message = get_phone(command)
            print(f"Contact's phone is {get_phone_message}")
        elif command.startswith('show all'):
            for key, value in phone_book.items():
                print('|{:^15}|{:^15}|'.format(key, value))
        elif command.startswith('good bye') or command.startswith('close') or command.startswith('exit'):
            print("Good bye!")
            break
        else:
            raise ValueError


main()
