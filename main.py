import sys
from create import create_file, create_folder, get_list, change_dir
from copy import copy_f
from del_f import delete
from save_info import log
from game1 import game1
from game2 import game2


log('Старт программы')
try:
    command = sys.argv[1]
except IndexError:
    print('Отсутствует параметр. help, ? - для подсказки ')
else:
    if command == 'list':
        get_list()
    elif command == 'chdir':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует имя дериктории')
        else:
            change_dir(name)
    elif command == 'mkfile':
        try:
            name = sys.argv[2]
            text = sys.argv[4]
        except IndexError:
            print('Отсутствует имя файла')
        else:
            create_file(name, text)
    elif command == 'mkfolder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует имя папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует имя')
        else:
            delete(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Отсутствует имя')
        else:
            copy_f(name, new_name)
    elif command == 'game':
        print('1 - "Угадай число загаданое компьютером" ')
        print('2 - "Компьютер угадает число загаданое тобой" ')
        answer = input('1 или 2 ?')
        if answer == '1':
            game1()
        elif answer == '2':
            game2()
        else:
            print('Непонял! ')
    elif command == 'help' or '?':
        print('list - список файлов и (или) папок ')
        print('mkfile name - саздать файл с именем name')
        print('mkfolder name - саздать папку с именем name')
        print('delete name - удалить папку или файл с именем name')
        print('copy name, new_name - копировать папку или  файл name с новым именем new_name')
        print('game - Игры')

log('Конец программы')
