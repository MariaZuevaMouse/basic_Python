def some_f():
    return 10


result = some_f()
print(result)

a = some_f  # func is written to a var
print(a)
print(type(a))

print(a())


# ________________________
def f():
    print('hello from other f')


def to(f_param):
    # param is a function
    f_param()


to(f)


# --------------------------

def my_filter(numbers):
    res = []
    for number in numbers:
        if number % 2 == 0:
            res.append(number)
    return res


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_filter(numbers))

def my_filter2(numbers, funcion):
    res = []
    for number in numbers:
        if funcion(number):
            res.append(number)
    return res

def is_even(number):
    return number % 2 == 0

def is_not_even(number):
    return number % 2 != 0

def grater_then_4(number):
    return number >4

print(my_filter2(numbers, is_even))
print(my_filter2(numbers, is_not_even))
print(my_filter2(numbers, grater_then_4))
