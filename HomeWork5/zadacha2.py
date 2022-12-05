# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def Konf(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, Не. Столько конфет брать не стоит "))
    return x

def Rez(name, k, counter, kolvo_konf):
    print(f"{name} взял {k} конфет, теперь у него {counter}./n На столе осталось: {kolvo_konf} конфет.")

user1 = input("Первый игрок: ")
user2 = input("Второй игрок: ")
kolvo_konf = 2021
flag = randint(0,2)
if flag:
    print(f"Первый ходит {user1}")
else:
    print(f"Первый ходит {user2}")

Konf_1P = 0 
Konf_2P = 0

while kolvo_konf > 28:
    if flag == True:
        k = Konf(user1)
        Konf_1P += k
        kolvo_konf -= k
        flag = False
        Rez(user1, k, Konf_1P, kolvo_konf)
    else:
        k = Konf(user2)
        Konf_2P += k
        kolvo_konf -= k
        flag = True
        Rez(user2, k, Konf_2P, kolvo_konf)

if flag:
    print(f"Победил {user1}")
else:
    print(f"Победил {user2}")
