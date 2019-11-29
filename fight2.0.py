name = input('Введите ваш ник: ')
player = {
    'name': name,
    'health': 100,
    'damage': 50,
    'armor': 1.2
}
enamy = {
    'name': 'Subzero',
    'health': 110,
    'damage': 51,
    'armor': 1.2
}
print(player, '\n','vs','\n', enamy,'\n')

def attack(user1, user2):
    user_attack = input('Удар (a)(j); Двойной удар (s)(k)')
    def arm(user):
          d = user['damage'] = int(user['damage']) / int(user['armor'])
          return d

    if user_attack == 'a':
        enamy['health'] = int(enamy['health'])-arm(player)
        print(player, '>>', enamy)
    elif user_attack == 's':
        enamy['health'] = int(enamy['health'])-(arm(player)+2)
        print(player, '>>', enamy)
    elif user_attack == 'j':
        player['health'] = int(player['health'])-arm(enamy)
        print(player, '<<', enamy)
    elif user_attack == 'k':
        player['health'] = int(player['health'])-(arm(enamy)+2)
        print(player, '<<', enamy)
    else:
        print('FIGHT!')


while (int(player['health']))>=0 and (int(enamy['health']))>=0:
    attack(player, enamy)

if int(player['health'])> 0:
    print(player,'\n', player['name'], 'is WIN!')
else:
    print(enamy,'\n', enamy['name'], 'is WIN!')