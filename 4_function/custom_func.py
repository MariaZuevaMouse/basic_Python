def print_separator0():
    print('-' * 100)


def print_separator1(sep):
    print(sep * 100)

def print_separator2(sep, sep_len):
    print(sep * sep_len)

def get_separator3(sep, sep_len):
    return sep* sep_len

print('First function')
print_separator0()
print('Repeat line')
print_separator1('*')
print_separator2('*', 10)
print_separator2('_', 5)

sep = get_separator3('_', 5)
text = 'Hello {}, Func {}'.format(sep, '0')

print(text)
# -------------------------------------

def hello(who):
    print('Hello, ', who)

hello('Karlos')
hello('Emily')

def greeting(say, who):
    print(say, who)

greeting('Hi ', 'Leo')
greeting('Hello', 'Max')
greeting(who='Mari', say='Hi')

#  default param
def greeting2(who, say='Hello'):
    print(say, who)

greeting2('Leo', 'Hi ')
greeting2('Leo')

# кортеж  - *who
def greeting3(say, *args):
    print(say, args)

greeting3('Hello', 'Leo', 'Kate', 'Tod')

# словарь
def get_person(**kwargs):
    for k,v in kwargs.items():
        print(k, v)

get_person(name='Leo', age=20, has_car=True)


