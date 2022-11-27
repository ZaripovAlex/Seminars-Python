# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def Peremnogalka(lst: list):
    rez = []
    if len(lst)%2 == 0:
        n=0
    else:
        n=1
    for i in range(int(len(lst)/2+n)):
        # print('i',lst[i])
        # print('-i-1',lst[-i-1])
        rez.append(lst[i]*lst[-i-1])
    return rez

list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]
rez=[]
rez=Peremnogalka(list1)
print(rez)
rez1=[]
rez1=Peremnogalka(list2)
print(rez1)


