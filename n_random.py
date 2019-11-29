import random


def n_rand(my_list):
    if my_list:
        n = (random.choice(my_list))
        return n
    # else:
    # return None


my_list = input('Введите список чисел, через пробел: ').split()
print('Случайное число: ', n_rand(my_list))
