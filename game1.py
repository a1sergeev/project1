import random


def game1():
    number = random.randint(1, 100)
    #print(number)
    user_number = None
    count = 0
    levels = {1: 10, 2: 5, 3: 3}
    level = int(input('Выберите уровень сложности (1,2,3): '))
    if level > 3 or level < 0:
        print("Уровни: 1) = 10 попыток, 2) = 5 попыток, 3) = 3 попытки")
        quit()
    else:
        max_count = levels[level]

    user_count = int(input('Введите количество игроков: '))
    users = []
    for i in range(user_count):
        user_name = input(f'Введите имя {i + 1}-го игрока: ')
        users.append(user_name)

    print(users)
    is_winner = False
    winner_name = None

    while not is_winner:
        count += 1
        if count > max_count:
            print('Все игроки проиграли :(')
            break
        print(f"Попытка № {count}")
        for user in users:
            print(f'Ход игрока {user}')
            user_number = int(input('Введите число: '))
            if user_number == number:
                is_winner = True
                winner_name = user
                break
            elif number < user_number:
                print('Ваше число больше загаданного')
            else:
                print('Ваше число меньше загаданного')
    else:
        print(f'Победа игрока {winner_name}!')
