
import pickle
import json


def serialize(my_text):
    answer = input('pickle or json: ')
    if answer == 'pickle':
        with open('file1.pickle', 'ab') as f:
            pickle.dump(my_text, f)
        print('Записанно в file1.pickle')
    elif answer == 'json':
        with open('file1.json', 'a', encoding='utf-8') as f:
            json.dump(my_text, f)
        print('Записанно в file1.json')
    else:
        print('Непонял', end=' ')
        serialize(my_text)


