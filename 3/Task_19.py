# Дана последовательность из целых чисел.
# вводим к и сдвигаем циклически на к - положительное число

# [1, 2, 3, 4, 5] k = 3
# [4, 5, 1, 2, 3]

# list = [1, 2, 3, 4, 5]
# k = int(input('Введите сдвиг: '))
# print(list)
# j = 4
# i = 0

# while j > 0:
#     temp = list[i]
#     list[i] = list[len(list) - 1]
#     list[len(list) - 1] = temp
#     i += 1
#     j -= 1
#     if j == 0 and k > 2:
#         i = 0
#         j = 4
#         k -= 1



# print(list)

list = [1, 2, 3, 4, 5]
k = int(input('Введите сдвиг: '))
print(list)
new_list = []
while k > 0:
    for i in list:
        new_list.append(list[- i])
    k -= 1
print(new_list)