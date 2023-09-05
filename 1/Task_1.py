# По данному целому неотрицательному n вычислите значение n!
# решаем с while

n = int(input("n = "))
count = 1
factorial = 1
while count <= n:
    factorial *= count
    count += 1
print(f'{n}! = {factorial}') 