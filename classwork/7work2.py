# import string
# import  random
# from random import randint
#
# letters = string.ascii_letters
#
# print(letters)
#
# some_int = randint(2, 9)
# print(some_int)


# ФУНКЦИИ
# def имя функции(параметры, если надо):
#    блок кода
# print()

def print_something():
    print("hello, world!!!!")

def print_dict(some_dict):
    for key in some_dict:
        print(f"'{key}': {some_dict[key]}")

points_dict = {"A": (1, 2),
               "B": (-2, 4),
               "C": (0, -6)}
print_dict(points_dict)