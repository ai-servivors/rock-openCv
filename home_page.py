import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
from time import strftime

window = tk.Tk()
window.geometry("511x513")
window.resizable(0,0)
window.title("Rock Paper Scissor")
bg = tk.PhotoImage(file = "rockk.png")
image_label = Label(window, image = bg)
image_label.place(x = -2, y = -2, relwidth = 1, relheight = 1)

def get_time() :
    string = strftime('%H:%M:%S %p')
    label_time.config(text = string)
    label_time.after(1000, get_time)

def show_input_field() :
    global input_name
    radio = tk.IntVar()
    name_label = tk.Label(window, text = "Name", font=('MALDINI', 15),
                          activebackground='#6AFFD6',
                          bg='#2286FF',
                          )
    name_label.place(x = 160, y = 415)
    input_name = tk.Entry(window, borderwidth = 4, width = 12)
    input_name.place(x = 230, y = 417)
    show_button = tk.Button(window, text = "Play",
                            font=('MALDINI', 15),
                            activebackground='#6AFFD6',
                            bg='#2286FF',
                            command = play)
    show_button.place(x = 330, y = 415)

def play() :
    global label_message1
    if not input_name.get() :
        label_message1 = tk.Label(text = 'Please Inter Your Name',
                                  font=('MALDINI', 15), bg='#2286FF')
        label_message1.pack()
    else :
        import windowTwo
        label_Name = tk.Label(text = f'Welcome {input_name.get()}',
                              font=('MALDINI', 15),  bg='#2286FF')
        label_Name.pack()
        if label_message1 is not None :
            label_message1.destroy()

def close_window() :
    window.destroy()

start_button = tk.Button(window, text = "Start",
                         font = ('MALDINI', 15),
                         activebackground = '#6AFFD6',
                         bg = '#2286FF',
                         command = show_input_field)
#3463FF
exit_button = tk.Button(window, text = "Exit ",
                        activebackground='#6AFFD6',
                        bg='#2286FF',
                        font = ('MALDINI', 15),
                        command = close_window)

start_button.place(x = 160, y = 350)
exit_button.place(x = 325, y = 350)

label_time = Label(window, font=('ds-digital', 15), foreground = 'black' )
label_time.place(x = 421, y = 488)
get_time()
window.mainloop()
