# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.

import random
result = []
cnt = 0
while cnt != 20:
    random_list = random.randrange(1, 100)
    result.append(random_list)
    cnt += 1
print(result)

################################################################

# 3) Создать функцию my_print, которая принимает строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***

def my_print(val):
    print(f"***{val}***")
    return val
my_print("I'm the string")

#################################################################

# 4)Создать функцию my_print, которая принимает строку и печатает ее
# с символами * НАД и ПОД строкой. КОЛИЧЕСТВО СИМВОЛОВ * РАВНО КОЛИЧЕСТВУ СИМВОЛОВ В СТРОКЕ
# Пример:
# my_str = 'I'm the string'
# Печатает
# **************
# I'm the string
# **************

def my_print(val):
    val = str(val)
    print(f"{len(val) * '*'}")
    print(f"{val}")
    print(f"{len(val) * '*'}")
    return val
my_print("I'm the string")

##################################################################

# 5) То же, что 4, но ответ должен выглядеть так:
# ********************
# ***I'm the string***
# ********************

def my_print(val):
    val = str(val)
    val = f"{'***'}{val}{'***'}"
    print(f"{len(val) * '*'}")
    print(f"{val}")
    print(f"{len(val) * '*'}")
    return val
my_print("I'm the string")

