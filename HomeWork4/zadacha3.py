# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

lst = [1, 1, 2, 3, 4, 4, 4, 5]

def Poisk(x:int, lst:list):
    count=0
    for i in range(len(lst)):
        if lst[i]==x:
            count+=1
    return count

rez=[]
for i in range(len(lst)):
    if Poisk(lst[i],lst)==1:
        rez.append(lst[i])
    
print(f'В списке {lst} неповторяющиеся элементы: - {rez}')