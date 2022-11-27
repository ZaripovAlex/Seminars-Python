# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def ToBin(dex:int):
    binn=''
    while dex > 0:
        binn = str(dex % 2)+binn 
        dex = dex // 2
    return binn



n=int(input('Введите число: ')) 
rez=ToBin(n)
print(f'Число {n} в десятичном, это {rez} в двоичном')

