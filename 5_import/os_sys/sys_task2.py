# В зависимости от параметра вызывать различные функции скрипта
# Параметр ping -> функция выводит pong
# 2 параметра name <Имя> -> функция приветствия пользователя
# параметр list: показать содержимое текущей директории

import sys, os

def pong():
    print(' -> pong')

def hello(name):
    print('Hello', name)

def get_info():
    print(os.listdir())

# get_info()

command = sys.argv[1]

if command =='ping':
    pong()
elif command == 'list':
    get_info()
elif command == 'name':
    name = sys.argv[2]
    hello(name)

# launch from terminal
#       $python .\5_import\os_sys\sys_task2.py  ping
#       $python .\5_import\os_sys\sys_task2.py  list
#       $python .\5_import\os_sys\sys_task2.py  name Mari



