# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def Drob (lst: list):
    temp=[]
    for i in range(len(list)):
        rez=(list[i]) % 1
        if (rez!=0):
            temp.append(round(rez,3))
    return temp

list = [1.1, 1.2, 3.1, 5, 11.01]
rez = []
rez = Drob(list)
maxx = max(rez)
minn = min(rez)
print(rez,'=>', maxx-minn)