# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.

# 4  | 1
# -------
# 3  | 2

x = int(input('Введите координату Х: '))
y = int(input('Введите координату Y: '))
if (x==0) and (y==0):
    print ('Точка 0')
elif (x==0):
    print ('Ось Y')
elif (y==0):
    print ('Ось X')
elif (x>0) and (y>0):
    print ('Первая четверть')
elif (x>0) and (y<0):
    print ('Вторая четверть')
elif (x<0) and (y<0):
    print ('Третья четверть')
else: 
    print ('Четвертая четверть')