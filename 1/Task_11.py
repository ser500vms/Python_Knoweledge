# Дано натуральное число А > 1. Определите,
# каким ро счету числом Фибоначчи оно является,
# т.е выведите такое число n, что фиб n=A. Если
# А не является числом Фиббоначи, вывидете число -1

# in = 5
# out = 6

# Мое решение:
a = int(input("Введите число фибоначчи: "))
fib1 = 0
fib2 = 1
fib3 = 1
fib_sum = 0
count = 2
if a == fib1:
    print("Введенное число является 0-м по счету")
elif a == fib2:
    print("Введенное число является 1-м по счету")
elif a > 1:
    while fib_sum < a:
        fib_sum = fib2 + fib3
        fib2 = fib3
        fib3 = fib_sum
        count += 1
    if fib_sum == a:
        print(f'Введенное число является {count}-м по счету')
    else:
        print("Такго числа фиббоначи нет") 

# Решение семинара 1
A = int(input('A = '))
a1 = 0
a2 = 1
next_a = 0
i = 2
while next_a < A:
    next_a = a1 + a2
    a1 = a2
    a2 = next_a
    i += 1
    if next_a > A:
        i = -1
print(i)

# Решение 2
A = int(input('A = '))
a1, a2 = 0, 1
i = 2
while a2 < A:
    a1, a2 = a2, a1 + a2
    i += 1
    if next_a > A:
        i = -1
print(i)