# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]



def Fibonacci(n:int):
    rez=[]
    ch1=1
    ch2=1
    for _ in range(n):
        rez.append(ch1)      
        ch1,ch2=ch2,ch1+ch2
        # print('ch1:', ch1,'ch2',ch2)
    ch3=0
    ch4=1    
    for _ in range(n+1):
        rez.insert(0,ch3)
        ch3,ch4=ch4,ch3-ch4
        # print('ch3:', ch3,'ch4',ch4)
    return rez

k = int(input('Введите чило: '))
rez=Fibonacci(k)
print(f'Для k={k} список будет выглядеть так: {rez}')

