# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# [1, 1, 2, 0, -1, 3 , 4 , 4]
# 6


list = [1, 1, 2, 0, -1, 3 , 4 , 4]
my_set = set(list)
print(len(my_set))

# list = []
# for _ in range(int(input('Сколько значений Вы хотите ввести?: '))):
#     list.append(int(input('Введите число: ')))
# print(list)

# i = 0
# new_list = []
# while i < len(list):
#     if list.count(list[i]) < 2:
#         new_list.append(list[i])
#         print(new_list)
#     i += 1
    
# print(len(new_list))

# new_list = []
# for num in list:
#     if num not in new_list:
#         new_list.append(num)
# print(len(new_list))    

# new_list = []
# for num in list:
#     if new_list.count(num) == 0:
#         new_list.append(num)
# print(len(new_list))    

