from tkinter import*
from tkinter import messagebox
myWindow=Tk()
myWindow.title("TicTacToe")
myWindow.config()

def btnClick(button):
    global playerX, count
    if button["text"]==""and playerX==True:
        button["text"]='X'
        playerX=False
        count+=1

ul = Button(myWindow, text="", width=6, height=3, font=('Helvica',24), bg = "light green")
um = Button(myWindow, text="", width=6, height=3, font=('Helvica',24), bg = "light yellow")
ur = Button(myWindow, text="", width=6, height=3, font=('Helvica',24), bg = "light green")
ml = Button(myWindow, text="", width=6, height=3, font=('Helvica',24), bg = "light yellow")
mm = Button(myWindow, text="", width=6, height=3, font=('Helvica',24), bg = "light green")
mr = Button(myWindow, text="", width=6, height=3, font=('Helvica',24), bg = "light yellow")
bl = Button(myWindow, text="", width=6, height=3, font=('Helvica',24), bg = "light green")
bm = Button(myWindow, text="", width=6, height=3, font=('Helvica',24), bg = "light yellow")
br = Button(myWindow, text="", width=6, height=3, font=('Helvica',24), bg = "light green")

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