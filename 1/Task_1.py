# По данному целому неотрицательному n вычислите значение n!
# решаем с while

# Вариант 1
n = int(input("n = "))
count = 1
factorial = 1
while count <= n:
    factorial *= count
    count += 1
print(f'{n}! = {factorial}') 

# Вариант 2
n = int(input("n = "))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(f'{n}! = {factorial}')