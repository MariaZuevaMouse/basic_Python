import random

number = random.randint(1, 100)
print(number)

count = 0
max_count = 3
user_input = None

while number !=  user_input:
    count +=1
    if count > max_count:
        print('Вы проиграли')
        break
    print(f'Попытка № {count}')
    user_input = int(input('Введите число: '))
    if number < user_input:
        print('Ваше число больше загаданного')
    elif number > user_input:
        print('Ваше число меньше загаданного')

else:  # выполняется если выход происходит по условию, но не выполняется,если по Brake
    print('Победа')