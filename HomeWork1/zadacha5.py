# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = int(input('Введите координату X первой точки: '))
y1 = int(input('Введите координату Y первой точки: '))
x2 = int(input('Введите координату X второй точки: '))
y2 = int(input('Введите координату Y второй точки: '))
dlinna = ((x1-x2) ** 2 + (y1 - y2) ** 2) ** (0.5)
print(f'Растояние между точками с координатами ({x1},{y1}) и ({x2},{y2}) -> {round(dlinna,2)}' )