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
#label_welcome = tk.Label(text = "Welcome to the Rock Paper Scissor game", font = ('Helvetica', 10) , bg = '#F68583')
#label_welcome.pack(pady = 50)


"""
def resizer(e) :
    global bg1, resizer_bg, new_bg
    bg1 = Image.open("rocc.jpg")
    resizer_bd = bg1.resize((e.width,e.height), Image.ANTIALIAS)
    new_bg = ImageTk.PhotoImage(resizer_bd)
    my_canvas.create_image(0, 0, image = new_bg, anchor='center')
"""
def get_time() :
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000, get_time)

def show_input_field() :
    global input_name
    radio = tk.IntVar()
    name_label = tk.Label(window, text = "Name")
    name_label.place(x = 200, y = 400)
    input_name = tk.Entry(window, borderwidth = 4, width = 12)
    input_name.place(x = 240, y = 400)
#    gender_label = tk.Label(window, text = "Gender").place(x = 150,y = 170)
#    radio_male = tk.Radiobutton(window, text="Male", variable=radio, value=1)
#    radio_male.place(x = 150, y = 190)
#    radio_female = tk.Radiobutton(window, text="Female", variable=radio, value=2)
#    radio_female.place(x = 150, y = 210)
#    show_button.place(x = 300, y = 200)
    show_button = tk.Button(window, text = "Go", command = play)
    show_button.place(x = 330, y = 400)

def play() :
    global label_message1
    if not input_name.get() :
        label_message1 = tk.Label(text = 'Please Inter Your Name')
        label_message1.pack()
    else:
        import windowTwo
        label_Name = tk.Label(text = f'Welcome {input_name.get()}')
        label_Name.pack()
        if label_message1 is not None :
            label_message1.destroy()

def close_window() :
    window.destroy()
    import windowTwo

start_button = tk.Button(window, text = "Start", command = show_input_field)
#start_button.grid(row = 40, column = 0, padx = 5)

exit_button = tk.Button(window, text = "Exit", command = close_window)
#exit_button.place(x = 300, y = 90)
#exit_button.grid(row = 40, column = 1, padx = 5)

start_button.place(x = 160, y = 350)
exit_button.place(x = 325, y = 350)

label = tk.Label(window)
label.pack()
label = Label(window, font=('ds-digital', 15), foreground = 'black' )
label.place(x = 421, y = 488)
#font = ('ds-digital', 15)
get_time()
window.mainloop()
#window.bind('<Configure>', resizer)
