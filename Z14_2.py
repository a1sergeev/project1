''' 2: Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих следующим условиям:
Элемент кратен 3,
Элемент положительный,
Элемент не кратен 4.
Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа.
 10-20 чисел в списке вполне достаточно.'''

#Генератор списков
#my_list = input('Введите список чисел: ').split()
my_list = [3, 9, 6, -1, -2, -9, 4, 8, 16]
print('result= ', [elem for elem in my_list if int(elem) >= 0 and int(elem)%3 == 0 and int(elem)%4 != 0])

#Тернарный оператор
'''
#Вариант 2 
result = []
for elem in my_list:
     elem = int(elem)
     result.append(elem) if elem % 3 == 0 and elem >= 0 and elem % 4 != 0 else print('', end='')
print('result= ', result)
'''


