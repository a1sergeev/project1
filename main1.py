import n_random #Z10_3
import mdir

list1 = input('Введите список чисел, через пробел: ').split()
print('Случайное число: ', n_random.n_rand(list1))

n = int(input('Сколько папок нужно?: '))
mdir.n_dir(n)

ans = input('Удаление y - да, n - нет ')
while ans == 'y':
    dir_name = input('Имя папки на удаление: ')
    mdir.del_dir(dir_name)
    ans = input('Удалить ещё?: y - да, n - нет ')
else:
    quit()

