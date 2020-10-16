# import calendar
# print(calendar.month(2020, 9))

# a = "geeksforgeeks"
#
# b = list(a)
# print(b)

# print((1 + 3)**2)

# print("hello \"world\"")
#

# print(input("what is your name? : "))

# a = input("Введите первое число : ")
# b = input("Введите второе число : ")
# print(int(a) + int(b))

# name = input('Ваше имя? : ')
# print(list(name))

# name = input('Введите ваше имя: ' )
# count = input('Сколько раз вывести Ваше имя?: ' )
#
# print( name * int(count ))

# name = input("Как тебя зовут, друг? : ")
# print ("Пошёл ты нахуй, " + name)

# test = "string"
# test2 = 3
# print(test * test2)

# a = 55
# a-=25
# print(a)

password = input("Введи пароль, дорогуша: ")
if password == "123":
    print("Верный пароль, милости просим))")

    pogoda = input("Какая погода?(жарко, снег, дождь): ")
    time = input("Время суток(утро, день, вечер, ночь): ")
    print("Привет")
    if pogoda == "снег":
        print("Одевайся теплее, на улице идет снег")
        if time == "Утро":
            print("Позавтракала хоть?")
        elif time == "ночь":
            print("Красиво, когда ночью идёт снег")
        else:
            print("И гуляй на здоровье")
    if pogoda == "дождь":
        print("Возьми зонт, на улице дождь")
        if time == "ночь":
            print("Ночью, в дождь, не стоит идти")
        elif time == "Утро":
            print("Позавтракала хоть?")
        else:
            print("И гуляй на здоровье")
    if pogoda == "жарко":
        print("На улице жара")
        if time == "ночь":
            print("Днем будет вообще жопа")
        elif time == "утро":
            print("Кушать и на пляж?")
        elif time == "вечер":
            print("Срочно пивка холодненького!")
        else:
            print("Лучше поспать под кондёром")
    print("Удачи")
else:
    print("Пароль не верный. Давай, досвиданья!")

