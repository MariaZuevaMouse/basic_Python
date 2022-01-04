
name = input('who is the creator of python?')
# answer = 'Guido van Rossum'
answer = 'Guido'

while name != answer:
    print('Incorrect')
    name = input('who is the creator of python?')

print('Correct')

number = 0
n = int(input('Enter a number n: '))

while number <= n:
    if number % 2 == 0:
        print(number)
    # number = number + 1
    number += 1
