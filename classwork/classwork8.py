# import os
# from utils import get_distance, get_area_gerone

point_A = (10, 1)
point_B = (10, 2)
dist_A_B = get_distance(point_A, point_B)
print(dist_A_B)



point_A = (10, 1)
point_B = (10, 2)
point_C = (9, 1)
area_a_b_c = get_area_gerone(point_A, point_B, point_C)

assert abs(area_a_b_c - 0.5) < 0.001   #если True, то программа идет дальше(проверка). abc - модуль
assert abs(get_area_gerone((0, 0), (0, 4), (3, 0)) - 6.0) < 0.001
assert abs(get_distance((0, 4), (3, 0)) - 5.0) < 0.01
print(area_a_b_c)

print(os.listdir()) #печатаем наши директории


some = ["homework7", "homework8", "homework"]
my_str = "$$$".join(some)
print(my_str)

