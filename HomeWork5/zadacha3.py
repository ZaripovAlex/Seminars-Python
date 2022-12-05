# Создайте программу для игры в ""Крестики-нолики"".

from tkinter import *
from tkinter import messagebox


root = Tk()
def PobedaX():
    if (rez[0]==1 and rez[1]==1 and rez[2]==1) or \
       (rez[3]==1 and rez[4]==1 and rez[5]==1) or \
       (rez[6]==1 and rez[7]==1 and rez[8]==1) or \
       (rez[0]==1 and rez[3]==1 and rez[6]==1) or \
       (rez[1]==1 and rez[4]==1 and rez[7]==1) or \
       (rez[2]==1 and rez[5]==1 and rez[8]==1) or \
       (rez[0]==1 and rez[4]==1 and rez[8]==1) or \
       (rez[6]==1 and rez[4]==1 and rez[2]==1):
            root.quit()
            messagebox.showinfo('Победа!!!', 'Победили КРЕСТИКИ!')

def PobedaO():
    if (rez[0]==0 and rez[1]==0 and rez[2]==0) or \
       (rez[3]==0 and rez[4]==0 and rez[5]==0) or \
       (rez[6]==0 and rez[7]==0 and rez[8]==0) or \
       (rez[0]==0 and rez[3]==0 and rez[6]==0) or \
       (rez[1]==0 and rez[4]==0 and rez[7]==0) or \
       (rez[2]==0 and rez[5]==0 and rez[8]==0) or \
       (rez[0]==0 and rez[4]==0 and rez[8]==0) or \
       (rez[6]==0 and rez[4]==0 and rez[2]==0):
            root.quit()
            messagebox.showinfo('Победа!!!', 'Победили НОЛИКИ!')

def hodX (a):
    if a==0:
        btn0.configure(text="X", bg="green" )
        rez[a]=1
        PobedaX()
    elif a==1:
        btn1.configure(text="X", bg="green" )
        rez[a]=1
        PobedaX()
    elif a==2:
        btn2.configure(text="X", bg="green" )
        rez[a]=1
        PobedaX()
    elif a==3:
        btn3.configure(text="X", bg="green" )
        rez[a]=1
        PobedaX()
    elif a==4:
        btn4.configure(text="X", bg="green" )
        rez[a]=1
        PobedaX()
    elif a==5:
        btn5.configure(text="X", bg="green" )
        rez[a]=1
        PobedaX()
    elif a==6:
        btn6.configure(text="X", bg="green" )
        rez[a]=1
        PobedaX()
    elif a==7:
        btn7.configure(text="X", bg="green" )
        rez[a]=1
        PobedaX()
    elif a==8:
        btn8.configure(text="X", bg="green" )
        rez[a]=1
        PobedaX()
    else:
        print("Что то пошло не так")
    print(rez)

def hodO (a):
    if a==0:
        btn0.configure(text="O", bg="red" )
        rez[a]=0
        PobedaO()
    elif a==1:
        btn1.configure(text="O", bg="red" )
        rez[a]=0
        PobedaO()
    elif a==2:
        btn2.configure(text="O", bg="red" )
        rez[a]=0
        PobedaO()
    elif a==3:
        btn3.configure(text="O", bg="red" )
        rez[a]=0
        PobedaO()
    elif a==4:
        btn4.configure(text="O", bg="red" )
        rez[a]=0
        PobedaO()
    elif a==5:
        btn5.configure(text="O", bg="red" )
        rez[a]=0
        PobedaO()
    elif a==6:
        btn6.configure(text="O", bg="red" )
        rez[a]=0
        PobedaO()
    elif a==7:
        btn7.configure(text="O", bg="red" )
        rez[a]=0
        PobedaO()
    elif a==8:
        btn8.configure(text="O", bg="red" )
        rez[a]=0
        PobedaO()
    else:
        print("Что то пошло не так")
    print(rez)

root.title("Крестики - Нолики")
root.geometry("450x480")
root.resizable(width=False,height=False)
rez=[-1,-1,-1,-1,-1,-1,-1,-1]
btn0 = Button(height=10, width=20, text="1")
btn0.bind('<Button-1>',lambda a: hodX(0))
btn0.bind('<Button-3>',lambda btn0: hodO(0))
btn0.grid(row=1,column=1)
btn1 = Button(height=10, width=20, text="2")
btn1.grid(row=1,column=2)
btn1.bind('<Button-1>',lambda a: hodX(1))
btn1.bind('<Button-3>',lambda btn0: hodO(1))
btn2 = Button(height=10, width=20, text="3")
btn2.grid(row=1,column=3)
btn2.bind('<Button-1>',lambda a: hodX(2))
btn2.bind('<Button-3>',lambda btn0: hodO(2))
btn3 = Button(height=10, width=20, text="4")
btn3.grid(row=2,column=1)
btn3.bind('<Button-1>',lambda a: hodX(3))
btn3.bind('<Button-3>',lambda btn0: hodO(3))
btn4 = Button(height=10, width=20, text="5")
btn4.grid(row=2,column=2)
btn4.bind('<Button-1>',lambda a: hodX(4))
btn4.bind('<Button-3>',lambda btn0: hodO(4))
btn5 = Button(height=10, width=20, text="6")
btn5.grid(row=2,column=3)
btn5.bind('<Button-1>',lambda a: hodX(5))
btn5.bind('<Button-3>',lambda btn0: hodO(5))
btn6 = Button(height=10, width=20, text="7")
btn6.grid(row=3,column=1)
btn6.bind('<Button-1>',lambda a: hodX(6))
btn6.bind('<Button-3>',lambda btn0: hodO(6))
btn7 = Button(height=10, width=20, text="8")
btn7.grid(row=3,column=2)
btn7.bind('<Button-1>',lambda a: hodX(7))
btn7.bind('<Button-3>',lambda btn0: hodO(7))
btn8 = Button(height=10, width=20, text="9")
btn8.grid(row=3,column=3)
btn8.bind('<Button-1>',lambda a: hodX(8))
btn8.bind('<Button-3>',lambda btn0: hodO(8))


root.mainloop()