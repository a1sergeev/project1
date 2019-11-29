#
import pickle
import json

def deserialize():
    file_name = input('Введите имя файла: ')
    if '.pickle' in file_name:
        with open('{}'.format(file_name), 'rb') as f:
            file_text = pickle.load(f)
        print(file_text)
        print('Прочитанно из {}'.format(file_name))
    elif '.json' in file_name:
        with open('{}'.format(file_name), 'r', encoding='utf-8') as f:
            file_text = json.load(f)
        print(file_text)
        print('Прочитанно из {}'.format(file_name))
    else:
        print('Непонял.', end=' ')
        deserialize()

