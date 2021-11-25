import tkinter as tk
window = tk.Tk()
window.geometry("400x250")
window.title("Rock Paper Scissor")
label_welcome = tk.Label(text="Welcome to the Rock Paper Scissor game").pack()

def show_input_field() :
    global input_name
    radio = tk.IntVar()
    input_name = tk.Entry(window,borderwidth=4,width=12)
    input_name.place(x=190, y=140)
    name_label = tk.Label(window, text = "Name").place(x = 150,y = 140)
    gender_label = tk.Label(window, text = "Gender").place(x = 150,y = 170)

    radio_male = tk.Radiobutton(window, text="Male", variable=radio, value=1)
    radio_male.place(x = 150, y = 190)

    radio_female = tk.Radiobutton(window, text="Female", variable=radio, value=2)
    radio_female.place(x = 150, y = 210)
    show_button.place(x = 300, y = 200)

def play():
    global label_message1
    if not input_name.get() :
        label_message1 = tk.Label(text='Please Inter Your Name')
        label_message1.pack()
    else :
        import windowTwo
        label_Name = tk.Label(text=f'Welcome {input_name.get()}')
        label_Name.pack()
        if label_message1 is not None :
            label_message1.destroy()

def close_window():
    window.destroy()
    import windowTwo

start_button = tk.Button(window,text = "Start", command= show_input_field, activeforeground = "red",activebackground = "blue",pady=10,padx=20)
exit_button = tk.Button(window,text = "Exit",command = close_window ,activeforeground = "red",activebackground = "blue",pady=10,padx=20)

show_button = tk.Button(window,text = "Go", command= play, activeforeground = "red",activebackground = "blue",pady=10,padx=20)

start_button.place(x = 50, y = 90)
exit_button.place(x = 300, y = 90)
label = tk.Label(window)
label.pack()
window.mainloop()
