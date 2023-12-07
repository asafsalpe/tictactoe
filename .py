from cProfile import label
from cgitb import text
from pickle import GLOBAL
from tkinter import*
from tkinter import messagebox

myWindow=Tk()
myWindow.title("TicTacToe")
myWindow.config()

playerX = True
count = 0

def disableButtons():
    ul.config(state=DISABLED)
    um.config(state=DISABLED)
    ur.config(state=DISABLED)
    ml.config(state=DISABLED)
    mm.config(state=DISABLED)
    mr.config(state=DISABLED)
    bl.config(state=DISABLED)
    bm.config(state=DISABLED)
    br.config(state=DISABLED)
    return 0

def reset():
    global count
    count = 0
    ul.config(state=NORMAL)
    um.config(state=NORMAL)
    ur.config(state=NORMAL)
    ml.config(state=NORMAL)
    mm.config(state=NORMAL)
    mr.config(state=NORMAL)
    bl.config(state=NORMAL)
    bm.config(state=NORMAL)
    br.config(state=NORMAL)
    ul["text"]=''
    um["text"]=''
    ur["text"]=''
    bl["text"]=''
    bm["text"]=''
    br["text"]=''
    ml["text"]=''
    mm["text"]=''
    mr["text"]=''
    
    return 0 

def infoWindow():
    newWindow=Toplevel()
    newWindow.title('Rules')
    newWindow.geometry('1015x200')
    newWindow.config(bg = "#FFE0E0")
    description=Label(newWindow, text="Rules", font = "Helvica 24 bold")
    description.grid(row = 0, column = 0)
    description=Label(newWindow, text = "The object of Tic Tac Toe is to get three in a row", font = "Helvica 14")
    description.grid(row=1, column = 0)
    description=Label(newWindow, text = "You play on a three by three game board", font = "Helvica 14")
    description.grid(row = 2, column = 0)
    description=Label(newWindow, text = "The first player is known as X and the second is O", font = "Helvica 14")
    description.grid(row=3, column=0)
    description=Label(newWindow, text="Players alternate placing Xs and Os on the game board until either oppent has three in a row or all nine squares are filled", font = "Helvica 14")
    description.grid(row = 4, column = 0)
    description=Label(newWindow, text = "X always goes first, and in the event that no one has three in a row, the stalemate is called a cat game", font = "Helvica 14")
    description.grid(row=5, column =0)
    return 0

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
        disableButtons()
        
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
        disableButtons()
        
    elif count==9 and winner==False:
        messagebox.showinfo("TicTacToe", "Draw")
        disableButtons()
        return 0 

ul = Button(myWindow, text="", width=6, height=3, font=('Helvica 24 bold'), command=lambda:btnClick(ul))
um = Button(myWindow, text="", width=6, height=3, font=('Helvica 24 bold'), command=lambda:btnClick(um))
ur = Button(myWindow, text="", width=6, height=3, font=('Helvica 24 bold'), command=lambda:btnClick(ur))
ml = Button(myWindow, text="", width=6, height=3, font=('Helvica 24 bold'), command=lambda:btnClick(ml))
mm = Button(myWindow, text="", width=6, height=3, font=('Helvica 24 bold'), command=lambda:btnClick(mm))
mr = Button(myWindow, text="", width=6, height=3, font=('Helvica 24 bold'), command=lambda:btnClick(mr))
bl = Button(myWindow, text="", width=6, height=3, font=('Helvica 24 bold'), command=lambda:btnClick(bl))
bm = Button(myWindow, text="", width=6, height=3, font=('Helvica 24 bold'), command=lambda:btnClick(bm))
br = Button(myWindow, text="", width=6, height=3, font=('Helvica 24 bold'), command=lambda:btnClick(br))

major=Menu(myWindow)
myWindow.config(menu=major)

options=Menu(major, tearoff=False)
major.add_cascade(label="Options", menu=options)
options.add_command(label="Play again", command=reset)
options.add_command(label="Close", command=myWindow.quit)
major.add_command(label="Rules",command=infoWindow)







ul.grid(column = 0, row = 0)
um.grid(column = 0, row = 1)
ur.grid(column = 0, row = 2)
ml.grid(column = 1, row = 0)
mm.grid(column = 1, row = 1)
mr.grid(column = 1, row = 2)
bl.grid(column = 2, row = 0)
bm.grid(column = 2, row = 1)
br.grid(column = 2, row = 2)

ul.config(bd=8, bg = "#F4C2C2")
um.config(bd=8, bg = "#FFE0E0")
ur.config(bd=8, bg = "#F4C2C2")
ml.config(bd=8, bg = "#FFE0E0")
mm.config(bd=8, bg = "#F4C2C2")
mr.config(bd=8, bg = "#FFE0E0")
bl.config(bd=8, bg = "#F4C2C2")
bm.config(bd=8, bg = "#FFE0E0")
br.config(bd=8, bg = "#F4C2C2")

myWindow.mainloop()