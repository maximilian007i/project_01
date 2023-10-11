from tkinter import *
import random
from tkinter import messagebox
def no():
    messagebox.showinfo(" ", "Cпасибо! Ваш голос учтён!")
    quit()
def motionMouse(event):
    btn.place(x=random.randint(0, w - btn.winfo_reqwidth()), y=random.randint(0, h))
def pressMouse(event):
    quit(0)
root = Tk()
root.attributes('-fullscreen', True)
root.resizable(False, False)
root.configure(bg="#000000")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
lab = Label(text="Хотите ли вы увеличение зарплаты?", font="Arial 20").place(x=500, y=300)
btn1 = Button(text="Нет", font="Arial 20", command=no).place(x=600, y=432)
btn = Button(text="Да", font="Arial 20")
btn.place(x=w // 2 - btn.winfo_reqwidth() // 2, y=h // 2)
btn.bind("<Enter>", motionMouse)
root.mainloop()
