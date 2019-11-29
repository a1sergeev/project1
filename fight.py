'''
3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
name - строка полученная от пользователя,
health = 100,
damage = 50.
### Поэкспериментируйте с значениями урона и жизней по желанию.
### Теперь надо создать функцию attack(person1, person2).
Примечание: имена аргументов можете указать свои.
### Функция в качестве аргумента будет принимать атакующего и атакуемого.
### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
Функция должна сама работать со словарями и изменять их значения.
'''
name = input('Введите ваш ник: ')
player = {
    'name': name,
    'health': 100,
    'damage': 50
}

enamy = {
    'name': 'Subzero',
    'health': 110,
    'damage': 51
}
print(player, '\n','vs','\n', enamy,'\n')

def attack(user1, user2):
    user_attack = input('Удар (a)(j); Двойной удар (s)(k)')
    if user_attack == 'a':
        enamy['health'] = int(enamy['health'])-int(player['damage'])
        print(player, '>>', enamy)
    elif user_attack == 's':
        enamy['health'] = int(enamy['health'])-int(player['damage']+2)
        print(player, '>>', enamy)
    elif user_attack == 'j':
        player['health'] = int(player['health'])-int(enamy['damage'])
        print(player, '<<', enamy)
    elif user_attack == 'k':
        player['health'] = int(player['health'])-int(enamy['damage']+2)
        print(player, '<<', enamy)
    else:
        print('FIGHT!')


while (int(player['health']))>=0 and (int(enamy['health']))>=0:
    attack(player, enamy)

if int(player['health'])> 0:
    print(player,'\n', player['name'], 'is WIN!')
else:
    print(enamy,'\n', enamy['name'], 'is WIN!')