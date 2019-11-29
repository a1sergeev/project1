import os, shutil


def copy_f(name, new_name):
    try:
        shutil.copytree(name, new_name) if os.path.isdir(name) else shutil.copy(name, new_name)
    except FileExistsError:
        print('Уже существует ')


if __name__ == '__main__':
    copy_f('text.dat', 'new_f.txt')
