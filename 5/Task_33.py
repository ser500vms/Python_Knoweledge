# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def max_num(list):
    max = 1
    for i in range(len(list)):
        if max < grades[i]:
            max = grades[i]
    return max

def min_num(list):
    min = 5
    for i in range(len(list)):
        if min > grades[i]:
            min = grades[i]
    return min

grades = [1, 3, 3, 3, 4, 5, 5]
print(grades)

def change_gardes(list, num):
    min = min_num(grades)
    max = max_num(grades)
    for i in range(len(list)):
        if max == list[i]:
            list[i] = min 
    return list   

print(change_gardes(grades, 5))


