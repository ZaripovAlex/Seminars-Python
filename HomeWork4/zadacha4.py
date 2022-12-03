# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

from random import randint
with open('rez.txt', 'w') as data:
    rez=''
    k=int(input('Введите натуральную степень k: '))
    for i in range(k,-1,-1):
        a=randint(0,10)
        if i ==0:
            if a!=0:
                rez=rez+f'+{a}=0'
        elif i==1:
            if a!=0:
                rez=rez+f'{a}*x'
        else:
            if a!=0:
                rez=rez+ f'{a}*(x**{i})+'
    data.writelines(rez)

print(rez)