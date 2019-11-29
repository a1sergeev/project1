import random


def game2():
    max_num = 100
    min_num = 1
    user_data = None
    o = input(' Загадай число от 1 до 100, а я угадаю. Нажми любую клавишу когда будешь готов')
    while min_num <= max_num:
        number = random.randint(min_num, max_num)
        print(number, '?', end="\t ")
        user_data = input('Твое число больше(>), меньше(<) или равно(=)? -|')
        if user_data == '>':
            min_num = number + 1
        elif user_data == '<':
            max_num = number - 1
        elif user_data == "=":
            print(number, "Угадал!")
            break
        else:
            print("Я не понимаю, вводи только >, <, =. ")
    else:
        print("Так не бывает :(")
