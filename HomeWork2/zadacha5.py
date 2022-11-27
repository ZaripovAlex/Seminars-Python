# Реализуйте алгоритм перемешивания списка.
from random import randint

list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
temp=0
print('Исходный список', list)
for i in range(len(list)):
   random_index=randint(0,len(list)) 
   temp = list[i]
   list[i] = list[random_index]
   list[random_index]=temp
print('Перемешанный список', list)

