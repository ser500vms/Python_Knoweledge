# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


def power(a, b):
    pow = 1
    if b == 1:
        pow *= a
        return pow
    if b > 1:
        pow *= a * power(a, b - 1)
        return pow

a = 2
b = 3    
print(power(a, b))

    
