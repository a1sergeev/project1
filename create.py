import os


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        new_path = os.path.join(os.getcwd(), '{}'.format(name))
        os.mkdir(new_path)
        print("Каталог {} создан".format(name))
    except FileExistsError:
        print("Невозможно создать каталог, он уже существует! ")


def get_list():
    result = os.listdir()
    folders_only = input('dir - только папки, иначе и файлы и папки: ').lower()
    if folders_only == 'dir':
        result = [f for f in result if os.path.isdir(f)]
    [print(folder, end='\n') for folder in result]


def change_dir(name):
    # create_folder(name)
    os.chdir(name)
    print(os.getcwd())


if __name__ == '__main__':
    create_file('text.dat')
    create_file('text.dat', 'some text 26.11.2019')
    create_folder('new_folder')
    get_list()
