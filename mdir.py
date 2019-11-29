import os


def n_dir(amt):
    try:
        for i in range(amt):
            new_path = os.path.join(os.getcwd(), 'dir_{}'.format(i + 1))
            os.mkdir(new_path)
            print("Каталог dir_{} создан".format(i + 1))
    except IOError:
        print("Невозможно создать каталог, он уже существует! ")


def del_dir(name):
    answer = input('Удалить папку {}, y - да, n - нет: '.format(name))
    if answer == 'y':
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}'.format(name))
        os.rmdir(path)
    else:
        quit()

# n_dir(3)
# del_dir('dir_1')
# del_dir('dir_2')
# del_dir('dir_3')
