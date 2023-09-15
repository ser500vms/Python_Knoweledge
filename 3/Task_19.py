# Дана последовательность из целых чисел.
# вводим к и сдвигаем циклически на к - положительное число

# [1, 2, 3, 4, 5] k = 3
# [3, 4, 5, 1, 2]

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

# numbers = [1, 2, 3, 4, 5]
# k = 3
# k = k % len(numbers) # убираем лишнии итерации цикла

#Вариант №1
# list_result = []
# len_list = len(numbers)
# for i in range(len_list - k, len_list):
#     list_result.append(numbers[i])
# for i in range(len_list - k):
#     list_result.append(numbers[i])
# print(list_result)

#Вариант №2
# list_result = []
# for i in range(len(numbers)):
#     list_result.append(numbers[-k + i])
# print(list_result)

#Вариант №3
# for _ in range(k):
#     numbers.insert(0, numbers.pop())
# print(numbers)

#Вариант №4

# print(numbers[-k:] + numbers[:-k])

numbers = [1, 2, 3, 4, 5, 5]
my_set = set(numbers)
print(numbers)
print(my_set)