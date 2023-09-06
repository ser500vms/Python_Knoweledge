# генерируем случайные целые числа и ищем мин и макс
import random

N = int(input('Введите колличество арбузов: '))
watermelon = []
i = 0

for _ in range(N):
    watermelon.insert(i, random.randint(5, 35))

print(watermelon)

min = watermelon[i]
max = watermelon[i]
for _ in range(N - 1):
    if min > watermelon[i + 1]:
        min = watermelon[i + 1]
    if max < watermelon[i + 1]:
        max = watermelon[i + 1]
    i += 1

print(f'{min}, {max}')

# min = float('inf') - бесконечность с плюсом
# max = float('-inf')