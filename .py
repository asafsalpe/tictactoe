from tkinter import*
from tkinter import messagebox
myWindow=Tk()
myWindow.title("TicTacToe")
myWindow.config()

playerX = True
count = 0

def btnClick(button):
    global playerX, count
    if button["text"]==""and playerX==True:
        button["text"]='X'
        playerX=False
        count+=1
        checkWinner()
    elif button["text"]==""and playerX==False:
        button["text"]="O"
        playerX=True
        count+=1
        checkWinner()
    else:
        messagebox.showerror('TicTacToe', "Someone has already played here!")
    return 0

def checkWinner():
    global winner
    winner=False
    if (ul["text"]=='X' and um["text"]=='X'and ur["text"]=='X'or
        ml["text"]=='X' and mm["text"]=='X'and mr["text"]=='X'or
        bl["text"]=='X' and bm["text"]=='X'and br["text"]=='X'or
        ul["text"]=='X' and mm["text"]=='X'and br["text"]=='X'or
        ur["text"]=='X' and mm["text"]=='X'and bl["text"]=='X'or
        ul["text"]=='X' and ml["text"]=='X'and bl["text"]=='X'or
        um["text"]=='X' and mm["text"]=='X'and bm["text"]=='X'or
        ur["text"]=='X' and mr["text"]=='X'and br["text"]=='X'):
        winnner=True
        messagebox.showinfo("TicTacToe", "Player X wins!")
    elif (ul["text"]=='O' and um["text"]=='O'and ur["text"]=='O'or
        ml["text"]=='O' and mm["text"]=='O'and mr["text"]=='O'or
        bl["text"]=='O' and bm["text"]=='O'and br["text"]=='O'or
        ul["text"]=='O' and mm["text"]=='O'and br["text"]=='O'or
        bl["text"]=='O' and mm["text"]=='O'and ur["text"]=='O'or
        ul["text"]=='O' and ml["text"]=='O'and bl["text"]=='O'or
        um["text"]=='O' and mm["text"]=='O'and bm["text"]=='O'or
        ur["text"]=='O' and mr["text"]=='O'and br["text"]=='O'):
        winner=True
        messagebox.showinfo("TicTacToe", "Player O wins!")
    elif count==9 and winner==False:
        messagebox.showinfo("TicTacToe", "Draw")




ul = Button(myWindow, text="", width=6, height=3, font=('Helvica',24), command=lambda:btnClick(ul))
um = Button(myWindow, text="", width=6, height=3, font=('Helvica',24), command=lambda:btnClick(um))
ur = Button(myWindow, text="", width=6, height=3, font=('Helvica',24), command=lambda:btnClick(ur))
ml = Button(myWindow, text="", width=6, height=3, font=('Helvica',24), command=lambda:btnClick(ml))
mm = Button(myWindow, text="", width=6, height=3, font=('Helvica',24), command=lambda:btnClick(mm))
mr = Button(myWindow, text="", width=6, height=3, font=('Helvica',24), command=lambda:btnClick(mr))
bl = Button(myWindow, text="", width=6, height=3, font=('Helvica',24), command=lambda:btnClick(bl))
bm = Button(myWindow, text="", width=6, height=3, font=('Helvica',24), command=lambda:btnClick(bm))
br = Button(myWindow, text="", width=6, height=3, font=('Helvica',24), command=lambda:btnClick(br))

ul.grid(column = 0, row = 0)
um.grid(column = 0, row = 1)
ur.grid(column = 0, row = 2)
ml.grid(column = 1, row = 0)
mm.grid(column = 1, row = 1)
mr.grid(column = 1, row = 2)
bl.grid(column = 2, row = 0)
bm.grid(column = 2, row = 1)
br.grid(column = 2, row = 2)











myWindow.mainloop()