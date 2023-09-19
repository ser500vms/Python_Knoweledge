# Даны числа А и В выведите все числа в порядке возрастания если А < В
# или наоборот, решить рекурсией.


a, b = 1, 5
# def generate_list(a, b):
#     list = []
#     if a < b:
#         while a < b + 1:
#             list.append(a)
#             a += 1
#         return list
#     if a > b:
#         while a > b - 1:
#             list.append(a)
#             a -= 1
#         return list
# print(generate_list(a, b))

def generate_list(a, b):
    if a == b:
        return f'{a}'
    if a > b:
        return f'{a}, {generate_list(a - 1, b)}'
    if a < b:
        return f'{a}, {generate_list(a + 1, b)}'



print(generate_list(a, b))