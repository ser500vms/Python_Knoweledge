# печатаем уникальные значения в словаре

list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VII": "S007"}]

unique_keys = set()
for dict_item in list:
    for value_dict in dict_item.values():
        unique_keys.add(value_dict)
print(unique_keys)