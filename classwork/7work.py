# позиционное использование

# points_tuple = ((1, 2), (-2, 4), (0, -6))
# print(points_tuple[0])

# использование по имени

points_dict = {"A": (1, 2),
               "B": (-2, 4),
               "C": (0, -6)}
print(points_dict["A"])
# добавляем еще одну точку (point_D)
point_D = (3, 5)
points_dict["D"] = point_D

points_dict.update({"D1": point_D})

# d2 = {"D2": point_D}
# points_dict.update(d2)
# print(points_dict)
test_point = (5, 7)

if points_dict.get("D2") is None:
    points_dict["D2"] = test_point
print((points_dict))
value = points_dict["A"]
print((value))

for key in points_dict:
    print(key, points_dict[key])

print(list(points_dict.keys()))
print(list(points_dict.values()))












