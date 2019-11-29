def data(name, age, city):
    if age % 10 in (2, 3, 4):
        year = 'года'
    elif (age % 10 == 1) and (age % 100 != 11):
        year = 'год'
    else:
        year = 'лет'

    line_data = "{}, {} {}, проживает в городе {}".format(name, age, year, city)
    return (line_data)


name1 = input("Введите имя: ")
age1 = int(input("Введите возрост: "))
city1 = input("Ведите город: ")

if 0 < age1 and age1 < 111:
    print(data(name1, age1, city1))
else:
    print("Не верю что так много лет")
