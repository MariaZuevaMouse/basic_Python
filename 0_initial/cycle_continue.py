
#  brake  continue  while-else
# brake
name = None
answer = 'Guido'

while True:
    name = input('who is the creator of python?')
    if name == answer:
        break
    print('Incorrect')

print('Correct')

# continue
number = 0
n = int(input('Enter a number n: '))

while number <= n:
    if number % 2 == 0:
        number += 1
        continue
    print(number)
    number += 1


# while-else
number = 0

while number <= 100:
    print(number)
    number += 1
    # if number == 33:
    #     break
else:
    print('else end')

print('end')