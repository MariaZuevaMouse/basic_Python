import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir
from game_reverse import game_reverse
from game import game

save_info('Старт')
try:
    command = sys.argv[1]
    print(command)
except IndexError:
    print('Необходимо выбрать команду, используйте help для помощи')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует параметр - название файла, добавьте доп параметром имя файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует параметр - название папки, добавьте доп параметром имя папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует параметр - название папки/файла, добавьте доп параметром имя папки/файла для удаления')
        else:
            delete_file(name)
    elif command == 'cd':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует параметр - нужная директория, добавьте доп параметром директорию')
        else:
            change_dir(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Пропущены параметры, необходимо ввести имя папки/файла и имя копии файла/папки')
        else:
            copy_file(name, new_name)
    elif command == 'help':
        print('list - список файлов и папок ')
        print('create_file - создание файла ')
        print('create_folder - создание папки  ')
        print('delete - удаление файла или папки ')
        print('copy - опирование файла или папки  ')
    elif command == 'reverse':
        game_reverse()
    elif command == 'game':
        game()

    save_info('Конец')

# python .\main_script.py list
# python .\main_script.py help
# python .\main_script.py create_file test.txt
# python .\main_script.py create_folder new

