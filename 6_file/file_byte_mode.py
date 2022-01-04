#       Работа с файлом в режиме байтов
# open(‘filename’, ‘wb’) — режим записи байтов
# open(‘filename’, ‘rb’) — режим чтения байтов
# параметр encoding определяет кодировку
# open(‘filename’, ‘w’, encoding=’utf-8’)

with open('byte.txt', 'wb') as f:
    pass

with open('byte.txt', 'rb') as f:
    pass

with open('byte.txt', 'r', encoding='utf-8') as f:
    pass

#       Запись байтов в файл
# f.write(b’some bytes’) — файл открыт в режиме wb
# f.write(‘some str’) — файл открыт в режиме w
# в любом случае информация хранится в виде нулей и единиц
with open('byte.txt', 'wb') as f:
    f.write(b'Hello bytes')

with open('byte.txt', 'r', encoding='ascii') as f:
    print(f.read())

with open('byte.txt', 'wb') as f:
    str = 'Привет мир'
    f.write(str.encode('utf-8'))

with open('byte.txt', 'r', encoding='utf-8') as f:
    print(f.read())

#       Чтение байтов из файла
# f.read() - файл открыт в режиме rb — читаем байты
# f.read() - файл открыт в режиме r — читаем строки

with open('bytes.txt', 'wb') as f:
    str = 'Привет мир'
    f.write(str.encode('utf-8'))

with open('bytes.txt', 'w', encoding='utf-8') as f:
    f.write('Привет мир')

with open('bytes.txt', 'rb') as f:
    result = f.read()
    print(result)
    print(type(result))
    s= result.decode('utf-8')
    print(s)

with open('bytes.txt', 'a', encoding='utf-8') as f:
    f.write('Привет мир')

with open('bytes.txt', 'rb') as f:
    result = f.read()
    print(result)
    print(type(result))
    s= result.decode('utf-8')
    print(s)