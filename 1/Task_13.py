# оттепель когда среднесуточная > 0
# Пользователь вводит число N - общее количество рассматриваемых дней
# (1 <= N <= 100). В следующих строках распологается N целых чисел.
# Каждое число - среднесуточная температура в соответсвующий день. 
# Температуры - целые числа лежат в диапазоне от -50 до 50

# input 6 -> 20 30 -40 50 10 -10
# output 2
import random

N = int(input('N = '))

local_max = 0
global_max = 0
i = 0
x = []
for _ in range(N):
    x.insert(i, random.randint(-50, 50))
    if x[i] >= 0:
        local_max += 1
    else:
        if local_max > global_max:
            global_max = local_max
        local_max = 0

if local_max > global_max:
    global_max = local_max

print(x)
print(f'Количество дней с оттепелью - {global_max}')