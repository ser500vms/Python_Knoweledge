# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def count_del(num):
    i = 0
    count = 0
    while i < num:
        i += 1
        if num % i == 0:
            count += 1
    return(count)


def simple_num(num):
    if count_del(num) == 2:
        return 'yes'
    return 'no'
    

print(simple_num(12))
