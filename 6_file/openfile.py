#   Функция open
# открывает файл в указанном режиме
# f = open(‘my.txt’, ‘w’)
# file — имя файла
# mode — режим
# encoding — кодировка
#   Режимы открытия mode
# r — чтение
# w — запись, если файла нет, создается новый
# x — запись, если файла нет, ошибка
# a — дозапись
# b — двоичный режим
# + — открытие на чтение и запись

f = open('first.txt', 'w')

# f = open ('second.txt', 'r')  # error - file doesn't exist

f = open ('first.txt', 'r')

# Запись текста в файл
# write — записать строку в файл
# writelines — записать список строк в файл
# \n — символ конца строки

f = open('first.txt', 'w')
f.write('Hello\n')
f.write('World\n')

f.writelines(['Hello\n', 'Python\n'])

#     Чтение из файла
# read — чтение всего файла
# for line in f: — чтение файла построчно
# readlines — чтение файла в список строк

f = open('first.txt', 'r')

# print(f.read())

for line in f:
    print(line.replace('\n', ''))

# print(f.readlines())

f.close()
# ____________________________________________________

with open('first.txt', 'r') as f:
    for line in f:
        print(line.replace('\n', ''))

print('end')

