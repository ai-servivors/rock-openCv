from tkinter import *
window = Tk()
window.geometry("400x250")
window.title("Rock Paper Scissor")

name = Label(window, text = "Name").place(x = 150,y = 140)
gender = Label(window, text = "Gender").place(x = 150,y = 170)

e1 = Entry(window).place(x = 190, y = 140)
b1 = Button(window,text = "Start",activeforeground = "red",activebackground = "blue",pady=10,padx=20)
b2 = Button(window,text = "Exit",activeforeground = "red",activebackground = "blue",pady=10,padx=20)

b1.place(x = 50, y = 90)

b2.place(x = 300, y = 90)





radio = IntVar()
lbl = Label(text="Welcome to the game").pack()
R1 = Radiobutton(window, text="Male", variable=radio, value=1)
R1.place(x = 150, y = 190)
R2 = Radiobutton(window, text="Female", variable=radio, value=2)
                 # command=selection)
R2.place(x = 150, y = 210)


label = Label(window)
label.pack()
window.mainloop()
