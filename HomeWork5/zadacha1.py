# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'Я абв люблю абвЖвау иабв Питон'
lst = text.split()
# print(lst)
rez = list(filter(lambda i: not "абв" in i, lst))
print(rez)
