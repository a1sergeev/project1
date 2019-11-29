print("Медицинская анкета")
name = input('Имя: ')
last_name = input('Фамилия: ')
age = int(input('Возраст (лет): '))
mass = int(input('Вес (кг): '))
condition1 = 'хорошее состояние'
condition2 = 'следует заняться собой'
condition3 = 'следует обратиться к врачу'
if age < 30 and 50 < mass < 120:
    print(f' {name} {last_name}, {age} лет, {condition1} ')
elif (30 < age < 39) and (mass < 50 or mass > 120):
    print(f' {name} {last_name}, {age} лет, {condition2} ')
elif age > 40 and (mass < 50 or mass > 120):
    print(f' {name} {last_name}, {age} лет, {condition3} ')
elif age > 30 and 50 < mass < 120:
    print(f' {name} {last_name}, {age} лет, {condition1} ')
else:
    print(f' {name} {last_name}, {age} лет, {condition3} ')
'''
Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
Все остальные варианты вы можете обработать на ваш вкус и полет фантазии.
'''