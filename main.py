phone_book = {}


def hello(*args):
    return 'How can I help you?'


def close(*args):
    return "Good bye!"


def show_all(*args):
    result = ''
    for key, value in phone_book.items():
        result = result + '|{:^15}|{:^15}|\n'.format(key, value)
    return result


def add_or_change_phone(strip):
    words = strip.split(' ')
    if len(words) > 3:
        raise ValueError
    phone_book[words[1]] = words[2]
    return 'Phone saved'


def get_phone(strip):
    words = strip.split(' ')
    result = phone_book.get(words[1], 1)
    if result == 1:
        raise KeyError
    else:
        return f"Contact's phone is {result}"


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            inner(*args, **kwargs)
            return 'No phone for this contact, try again'
        except ValueError:
            inner(*args, **kwargs)
            return 'Enter correct command'
        except IndexError:
            inner(*args, **kwargs)
            return 'Enter correct username or phone'
    return inner


commands = {'hello': hello,
            'add': add_or_change_phone,
            'change': add_or_change_phone,
            'phone': get_phone,
            'show all': show_all,
            'good bye': close,
            'close': close,
            'exit': close}


@input_error
def main():
    while True:
        user_input = input('Enter your command: ')
        command = user_input.lower()
        commands_check = command.split(' ')
        if commands_check[0] in commands:
            result = commands[commands_check[0]]
            print(result(command))
            if command in ['good bye', 'close', 'exit']:
                break
        else:
            raise ValueError


output = main()
print(output)