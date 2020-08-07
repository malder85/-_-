# value = [1,2,3,4,5]
# value = tuple(value)
# print(type(value))


# values = [1, 2, 3, 4, 5]
# result = []
# for value in values[::-1]:
#     result.append(value)
# print(result)

# values = [1, 2, 3, 4, 5]
# new_value = values
# new_value.append(6)
# print(values)

# values = [0] * 6
# values[0] = 1
# print(values)

# value = 0
# values = [value] * 6
# value = 1
# print(values)

# my_list = [0]
# values = [my_list.copy()] * 3
# my_list.append(1)
# print(values)


# count = 10
# while count > 0:
#     print("test")
#     count -=1

# my_str = "fuckyou"
# my_list = []
# for symbol in my_str[::2]:
#     my_list.append(symbol)
# print(my_list)

# count = 10
# exit_flag = True
# while exit_flag:
#     count -= 1
#     if count > 0:
#         exit_flag = False
#     print("test")




# 1) У вас есть список my_list с значениями типа int. Распечатать те значения, которые больше 100. Задание выполнить с помощью цикла for.

# my_list = [1, 3, 5, 7, 9, 121, 170, 55, 490]
# for count in my_list:
#     if count > 100:
#         print(count)

######################################################################

# 2) У вас есть список my_list с значениями типа int, и пустой список my_results. Добавить в my_results те значения, которые больше 100. Распечатать список my_results. Задание выполнить с помощью цикла for.

# my_list = [1, 3, 5, 834, 7, 9, 121, 170, 55, 490]
# my_result = []
# for count in my_list:
#     if count > 100:
#         my_result.append(count)
# print(my_result)

######################################################################

# 3) У вас есть список my_list с значениями типа int. Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов. Количество элементов в списке можно получить с помощью функции len(my_list)

# my_list = [-5, -3, -1, 1, 3, 5, 834, 7, 9, 121, 170, 55, 490]
# if len(my_list) < 2:
#     my_list.append(0)
#     print(my_list)
# else:
#     new_my_list = my_list[-1] + my_list[-2]
#     my_list.append(new_my_list)
#     print(my_list)

#######################################################################

# 4) Пользователь вводит value - число с запятой (например 3.14) с клавиатуры. Вы приводите это value к типу float и выводите результат выражения value ** -1.
# Написать программу, которая вычисляет данное выражение и корректно обрабатывает возможные исключения.

try:
    value = input("Введите float число")
    value = float(value)
    print(value ** -1)
except ZeroDivisionError:
    print("Вы ввели 0. это не годится")
except ValueError:
    print("Число с запятой не подходит. Воспользуйтесь точкой ")







