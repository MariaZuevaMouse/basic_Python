# Модуль sys
# Взаимодействие с интерпретатором Python
# Функции и переменные sys:
#  - executable - путь к интерпретатору Python
#  - exit() - выход из Python
#  - platform - информация об ОС
#  - path - список путей поиска модулей
#  - argv - список аргументов командной строки
#  - and so on

import  sys

print(sys.executable)
print(sys.platform)
sys.exit()

print('Этот код уже не выполниться')
