phone_book = {}


def hello(*args):
    return 'How can I help you?'


def close():
    return "Good bye!"


def show_all(*args):
    result = ''
    for key, value in phone_book.items():
        result = result + '|{:^15}|{:^15}|\n'.format(key, value)
    return result.rstrip()


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
    elif len(words) != 2:
        raise ValueError
    else:
        return f"Contact's phone is {result}"


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
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


commands = {'hello': hello,
            'add': add_or_change_phone,
            'change': add_or_change_phone,
            'phone': get_phone,
            'show all': show_all,
            }


@input_error
def main():
    while True:
        user_input = input('Enter your command: ')
        command = user_input.lower()
        result = ''
        output = None
        if command in ['good bye', 'close', 'exit']:
            print(close())
            break
        for char in command:
            result += char
            if result in commands:
                output = commands[result](command)
                break
        if output is None:
            raise ValueError
        else:
            print(output)


main()
