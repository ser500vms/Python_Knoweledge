# ; Напишите программу, которая принимает на вход
# ; строку, и отслеживает, сколько раз каждый символ
# ; уже встречался. Количество повторов добавляется к
# ; символам с помощью постфикса формата _n.
# ; Input: a a a b c a a d c d d
# ; Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# ; Для решения данной задачи используйте функцию
# ; .split()
# string = 'a a a b c a a d c d d'
# print(string)
# list_split = string.split('a')
# print(list_split)

s = 'a a a b c a a d c d d'
s = s.split()
print(s)
# i = 0
# j = 1
# c = 1
# while i < len(s) - 1:
#     while j < len(s):
#         if s[i] == s[j]:
#             s.pop(j)
#             s.insert(j, f'{s[i]}_{c}')
#             j += 1
#             c += 1
#         else:
#             j += 1
#     c = 1
#     i += 1
#     j = i + 1
# print(s)

result = {}

for i in s:
    if i in result:
        print(f'{i}_{result[i]}', end=' ')
    else:
        print(i, end=' ')
    result[i] = result.get(i, 0) + 1

