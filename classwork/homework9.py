# 1) функции передаем полный путь к файлу в виде строки в формате "./path/to/file/filename.ext",
# где точка означает текущую директорию.
# (Это универсальный способ задать путь. Пользователи виндовс можете почитать это:
# https://stackoverflow.com/questions/2953834/windows-path-in-python)
# Функция возвращает два параметра: название файла и путь к папке.
# Пример использования:
# filename, folder_path = first_function(path)
#
import os
def name_and_path(path):
    full_path = os.path.join(name, path)




result = name_and_path("C:\\Users\\User\\PycharmProjects\\-_-\\classwork\\classwork10.py")


#######################################################

# 2) функции передаем полный путь к папке в виде строки в формате "./path/to/folder",
# где точка означает текущую директорию.
# Функция возвращает список ФАЙЛОВ из этой папки. Т.к. listdir возвращает файлы и подпапки,
# то такой функционал иногда нужен.
# Напомню, что есть метод os.path.isfile(path) который возвращает True, если path указывает на файл.
# И обратите внимание на "Щелчек Таноса" из классной работы. Мы там склеиваем путь с помощью os.path.join()
# Пример использования:
# files = second_function(path)
# Значение по умолчанию - текущая папка. Т.е. second_function() вернет файлы из текущей папки.

# import os
# def get_files(path):
#     files = []
#     values = os.listdir(path)
#     for value in values:
#         full_path = os.path.join(path, value)
#         if os.path.isfile(full_path):
#             files.append(full_path)
#     return files
#
# results = get_files("C:\\Users\\User\\PycharmProjects\\-_-\\classwork")



#####################################################

# 3) функции передаем полный путь к папке в виде строки в формате "./path/to/folder",
# где точка означает текущую директорию.
# Функция возвращает СЛОВАРЬ в формате: {"files": [список ФАЙЛОВ из папки], "folders": [список ПОДПАПОК из папки]}.
# Пример использования:
# path_dict = third_function(path)
# Значение по умолчанию - текущая папка. Т.е. third_function() вернет словарь с файлами и подпапками из текущей папки.

# def ret_dict