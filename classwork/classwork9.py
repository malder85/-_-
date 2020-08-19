# def modify_string_and_print(my_string: str, symbol="*", number=3):
#     my_string = f"{symbol * number}{my_string}{symbol * number}"
#     print(my_string)
#     return (my_string)
#
# def create_lines_under_above_string(my_string, symbol="*"):
#     add_str = symbol * len(my_string)
#     new_str = f"{add_str}\n{my_string}\n{add_str}"
#     print(new_str)

# mod_str = modify_string_and_print(("Some string"))
#
# create_lines_under_above_string(mod_str, "#")
# modify_string_and_print("Some string")
# modify_string_and_print("Some string", "$")
# modify_string_and_print("Some string", "%", 5)
# modify_string_and_print(number=5, my_string="Some string", symbol=".")

# def my_func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# my_func(1, "234", (1, 3, 4), {"qwe": 1, "asd": 4}, qwe=1, asd=4)


# file = open("README.md", 'r')
# lines = file.read()
# print(lines)
# file.close()
#
# with open("README.md", 'r') as file:
#     lines = file.read()
# print(lines)
# print("Hello")
#
# with open('test.txt', 'w') as file:
#     file.write('Hello!')
#     file.writelines(["asd", 'sdf'])

import  os

def create_folder(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass

def save_file(filename, path, data):
    filename_with_pat = os.path.join(path, filename)
    with open(filename_with_pat, 'w') as file:
        file.write(data)

create_folder('tmp')


alphabet = [chr(numb) for numb in range(ord('a'), ord('z') + 1)]
print(alphabet)
alphabet = "".join(alphabet)
print(alphabet)
save_string_to_file('alphabet.txt', 'tmp', alphabet)

for symbol in alphabet:
    save_string_to_file(f'{symbol}.txt', 'tmp', alphabet.replace((symbol, symbol.upper())))




