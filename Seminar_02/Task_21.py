# Задача №21. Решение в группах

# Напишите программу для печати всех уникальных
# значений в словаре.

# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

list_dicts = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]

unique_values = set()

for cur_dict in list_dicts:
    for key in cur_dict:
        unique_values.add(cur_dict[key].strip())

print(unique_values)

# или

unique_values2 = set()

for cur_dict in list_dicts:
    for key in cur_dict.keys():
        unique_values2.add(cur_dict[key].strip())

print(unique_values2)

# или

unique_values3 = set()

for cur_dict in list_dicts:
    for value in cur_dict.values():
        unique_values3.add(value.strip())

print(unique_values3)

# или

unique_values4 = set()

for cur_dict in list_dicts:
    unique_values4.add(*cur_dict.values())

print(unique_values4)

# или

unique_values5 = set()

for cur_dict in list_dicts:
    unique_values5.update(cur_dict.values())

print(unique_values5)