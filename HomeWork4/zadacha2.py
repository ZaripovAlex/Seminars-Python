# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def PrMn(n):
    rez = []
    i = 2
    while i ** 2 <= n: 
        while n % i == 0:
            n = n // i 
            rez.append(i)
        i += 1
    if n > 1:
        rez.append(n)
    return rez

i = int(input('Введите число: '))
print(i, '=', ' x '.join(str(x) for x in PrMn(i)))