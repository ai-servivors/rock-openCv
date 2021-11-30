import tkinter as tk
from tkinter.ttk import *
window3 = tk.Tk()
window3.geometry("511x550")
window3.title("Rock Paper Scissor")
bg1 = tk.PhotoImage(file="assets/gamerules.png")
image_label1 = Label(window3, image=bg1)
image_label1.pack()


def back_home() :
    window3.destroy()
    import home_page


back_button = tk.Button(window3, text = "Back ",
                        activebackground='#6AFFD6',
                        bg='#2286FF',
                        font = ('MALDINI', 15),
                        command = back_home)
back_button.place(x=230, y=500)

