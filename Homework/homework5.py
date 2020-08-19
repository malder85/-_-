# 2. Дано целое число (int). Определить сколько нулей в конце этого числа.

# numb = 251026000
# numb_str = str(numb)
# numb_str = numb_str[::-1]
# my_list = []
# x = 0
# for symbol in numb_str:
#     if symbol == "0":
#         my_list.append(symbol)
#     else:
#         break
# my_result = my_list.count("0")
# print(my_result)

######################################################

# 3. Даны списки my_list_1 и my_list_2. Создать список my_result в который вначале поместить четные элементы
# из my_list_1 и потом нечетные элементы из my_list_2.

# my_list_1 = ["qwerty"]
# my_list_2 = ["asdfgh"]
# my_result = []
# for symbol in my_list_1:
#     my_result.append(symbol[::2])
# for symbol in my_list_2:
#     my_result.append(symbol[1::2])
# print(my_result)

#####################################################

# 4. Дан список my_list.Создать список new_list у которого первый элемент из my_list стоит на последнем месте.Если
# my_list[1, 2, 3, 4], то new_list[2, 3, 4, 1]

# my_list = [1, 2, 3, 4]
# new_list = []
# new_list = my_list
# new_list.append(new_list.pop(0))
# print(new_list)



######################################################

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место. [1,2,3,4] -> [2,3,4,1].
# Пересоздавать список нельзя!

# my_list = [1, 2, 3, 4]
# for symbol in my_list:
#     my_list.insert(4, 1)
#     my_list.remove(1)
#     break
# print(my_list)

######################################################

# 7. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список. Если строка
# содержит нечетное количество символов, пропущенный второй символ последней пары должен быть заменен
# подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abc' -> ['ab', 'c_']

# my_str = "abc"
# len_my_str = int(len(my_str))
# my_str1 = f"['{my_str[0:2]}', '{my_str[2:]}']"
# my_str2 = f"['{my_str[0:2]}', '{my_str[2:]}_']"
# if len_my_str % 2 == 0:
#     print(my_str1)
# else:
#     print(my_str2)

#######################################################

# 8. Дана строка my_str в которой символы не повторяются и два символа l_limit, r_limit, которые точно находятся
# в этой строке. Причем l_limit левее чем r_limit. В переменную sub_str поместить часть строки между этими символами.
# my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"

# my_str = "My_long str"
# l_limit = my_str.find("o")
# r_limit = my_str.find("t")
# sub_str = my_str[l_limit + 1: r_limit]
# print(sub_str)









