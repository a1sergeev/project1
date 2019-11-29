import os


def delete(name):
    answer = input('Удалить {}, y - да, n - нет: '.format(name))
    if answer == 'y':
        os.rmdir(name) if os.path.isdir(name) else os.remove(name)
    else:
        quit()


if __name__ == '__main__':
    delete('text.dat')
