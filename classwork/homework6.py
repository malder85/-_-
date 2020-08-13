# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate.


# my_list = ["qwe", "123", "asd", "zxc"]
# my_list_new = []
#
# for index, value in enumerate(my_list):
#   if index % 2:
#     my_list_new.append(value[::-1])
#   else:
#     my_list_new.append(value)
# print(my_list_new)

#######################################################

# 4. Дан список my_list в котором могум быть как строки так и целые числа.
# Создать новый список в который поместить только строки из my_list.

# my_list = ["qwerty", "12345", "asdfg", "67890"]
# my_list_new = []
# for index, value in enumerate(my_list):
#     if type(value) == str:
#         my_list_new.append(value)
#     else:
#         pass
# print(my_list_new)


# my_list_new.append(value) for value in my_list if value = str(value)

#########################################################

# 5. Дана строка my_str. Вывести символы, которые встречаются в строке только один раз.

# my_str = "qweoppiuytrewasdfghjkllkjgfxcvbnmmnbvcxz"


