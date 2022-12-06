# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# AAAAAAFDDCCCCCCCAEEEEEEEEE
# 6A1F2D7C1A9E

def Arhiv (st: str) -> str:
    count = 1
    rez=''
    for i in range(len(st)-1):
        if st[i]==st[i+1]:
            count+=1
            #print(count, end=", ")
        else: 
            rez=rez+str(count)+st[i]
            #print (rez)
            count=1
    return rez+str(count)+st[-1] 
    

def Razarhiv (st: str) -> str:
    rez=''
    count = '' 
    for i in st:
        if i.isdigit():
            #print("i= ",i)
            count +=i            
        else:
            #print(count)
            rez = rez + i*int(count)
            count=''
    return rez



st1 = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEFF'
st2 = '6A1F2D7C1A14E'
n = int(input('Что будем делать. \n 1 - Архивировать: \n 2 - Разархивировать:\n -> '))
if n == 1:
    rez = Arhiv(st1)
elif n==2: 
    rez = Razarhiv(st2)
else:
    print('Эта функция не реализована')

print(rez)
