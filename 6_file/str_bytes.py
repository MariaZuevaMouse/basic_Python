#   Типы строк в Python
# str — обычные строки
# bytes — строки байт
# bytearray — изменяемая строка байт\

s= 'Hello Python'
print(type(s))

sb = b'Hello bytes'
print(type(sb))
print(sb)

#   Действия со строками байт
# индекс sb[0]
# срез sb[1:3]   and so on
print(s[1])
print('byte: ',sb[1])
print(sb[1:3])

for item in sb:
    print(item)

# ________ encoding
s = 'Hello Python'

sb = s.encode('ascii')
print(sb)
print(type(sb))

# --------

s = 'Hello Мир'

sb = s.encode('utf-8')
print(sb)
print(type(sb))

sb.decode('utf-8')
print(s)
print(type(s))



