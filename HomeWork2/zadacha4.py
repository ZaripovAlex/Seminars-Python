# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

n=int(input('Введите число: '))
list = []
for i in range(-n,n+1):
    list.append(i)
 
print(list)
rez=1
list2=[]
st=input('Введите индексы для произведения, разделите их пробелами: ')
st.split()
st.isdigit()
for i in range(len(st)):
    list2.append(st[i])
for i in list2:
    if i != ' ':
        rez=rez*list[int(i)]
print(rez)