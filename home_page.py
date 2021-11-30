import tkinter as tk
from tkinter.ttk import *
from time import strftime
from playsound import playsound

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
    playsound('BUTTON.wav')
    name_label = tk.Label(window, text = "Name", font=('MALDINI', 15),
                          activebackground='#6AFFD6',
                          bg='#2286FF',
                          )
    name_label.place(x = 160, y = 415)
    input_name = tk.Entry(window, borderwidth = 4, width = 20)
    input_name.place(x = 230, y = 417)
    Play_button = tk.Button(window, text = "Play By Mouse",
                            font=('MALDINI', 12),
                            activebackground='#6AFFD6',
                            bg='#2286FF',
                            command = play)
    Play_button.place(x = 150, y = 460)

    opencv_button = tk.Button(window, text="Play By Camera ",
                            font=('MALDINI', 12),
                            activebackground='#6AFFD6',
                            bg='#2286FF',command = play_camera)
    opencv_button.place(x=280, y=460)



def play() :
    global label_message1
    global name
    playsound('BUTTON.wav')
    name = input_name.get()
    if not name :
       pass
    else:
        window.destroy()
        import windowTwo

def play_camera() :
    playsound('BUTTON.wav')
    global label_message1
    global name
    name = input_name.get()
    if not name:
        pass
    else:
        window.destroy()
        playsound('camstart.mp3', block=False)
        import final_app

def close_window() :
#    window.destroy()
    playsound('BUTTON.wav')

def game_rules():
   window.destroy()
   import game_rules

start_button = tk.Button(window, text = "Start",
                         font = ('MALDINI', 15),
                         activebackground = '#6AFFD6',
                         bg = '#2286FF',
                         command = show_input_field)

exit_button = tk.Button(window, text = "Exit ",
                        activebackground='#6AFFD6',
                        bg='#2286FF',
                        font = ('MALDINI', 15),
                        command = close_window)

game_rule = tk.Button(window, text = "Game Rules",
                         font = ('MALDINI', 15),
                         activebackground = '#6AFFD6',
                         bg = '#2286FF',
                         command =game_rules)


start_button.place(x = 160, y = 350)
exit_button.place(x = 325, y = 350)

game_rule.place(x = 0, y = 0)

label_time = Label(window, font=('ds-digital', 15), foreground = 'black' )
label_time.place(x = 421, y = 488)
#get_time()

window.mainloop()

