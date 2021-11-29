import random
import tkinter as tk
from tkinter.ttk import *

windowTwo = tk.Tk()
windowTwo.geometry("1920x1080")
windowTwo.title("Page 2")

bg = tk.PhotoImage(file = "secondpage.png")
image_label = Label(windowTwo, image = bg)
image_label.place(x = -2, y = -2)

user_score = 0
computer_score = 0

def dont_play_again():
    windowTwo.destroy()
    import home_page

def go():

    global action
    global user_score
    global computer_score

    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    if options.get() == computer_action:
        computer_action= random.choice(possible_actions)
        global result
        result=tk.Label(windowTwo,font=("MALDINI", 15),
                        activebackground='#6AFFD6',
                        bg='#3D84B8',
                        text=f" Opps!! Both players selected {options.get()}. It's a tie! ")
        result.place(x=650, y=210)
    elif options.get() == "rock":
        if computer_action == "scissors":
            user_score+=1
            result=tk.Label(windowTwo,font=("MALDINI", 15),
                            activebackground='#6AFFD6',
                            bg='#3D84B8',
                            text="Rock smashes scissors! You win!")
            result.place(x=650, y=210)

        else:
            computer_score += 1
            result=tk.Label(windowTwo,font=("MALDINI", 15),
                            activebackground='#6AFFD6',
                            bg='#3D84B8',
                            text=" Paper covers rock! You lose. ")

            result.place(x=650, y=210)

    elif options.get() == "paper":
        if computer_action == "rock":
            result=tk.Label(windowTwo,font=("MALDINI", 15),
                            activebackground='#6AFFD6',
                            bg='#3D84B8',
                            text=" Paper covers rock! You win! ")
            user_score += 1
            result.place(x=650, y=210)
        else:
            computer_score += 1
            result=tk.Label(windowTwo,font=("MADLINI", 15),
                            activebackground='#6AFFD6',
                            bg='#3D84B8',
                            text=" Scissors cuts paper! You lose. ")
            result.place(x=650, y=210)
    elif options.get() == "scissors":
        if computer_action == "paper":
            result=tk.Label(windowTwo,font=("MALDINI", 15),
                            activebackground='#6AFFD6',
                            bg='#3D84B8',
                            text=" Scissors cuts paper! You win! ")
            user_score += 1
            result.place(x=650, y=210)

        else :
            computer_score += 1
            result=tk.Label(windowTwo,font=("MALDINI", 15),
                            activebackground='#6AFFD6',
                            bg='#3D84B8',
                            text=" Rock smashes scissors! You lose. ")
            result.place(x=650, y=210)

    def play_again():

        dest()

        play_again_button_yes.destroy()
        play_again_button_no.destroy()

        global user_score
        user_score = 0
        global computer_score
        computer_score = 0
        result4.destroy()
        result3 = tk.Label(windowTwo, font=("MALDINI", 15),
                           activebackground='#6AFFD6',
                           bg='#3D84B8',
                           text=f"  Your Score  {user_score}  :  Computer Score {computer_score}  ")
        result3.place(x=640, y=0)

    def dest():
            again_button.destroy()
            global show_button
            global result
            result.destroy()
            action.destroy()
            # user_action.delete(0, 10)
            show_button = tk.Button(windowTwo, text=" Go ", command=go,
                                    activebackground='#6AFFD6',
                                    bg='#2286FF',
                                    font=('MALDINI', 15),
                                    pady=10, padx=20)
            show_button.place(x=900, y=360)
    if user_score == 2 or computer_score == 2 :


        result4 = tk.Label(windowTwo,font=("MALDINI", 20),
                           activebackground='#6AFFD6',
                           bg='#3D84B8',
                           text=" Game Finished Wanna play again? ")
        result4.place(x=550, y=500)


        play_again_button_yes = tk.Button(windowTwo, text=" Yes ",command = play_again,
                                          font=("MALDINI", 15),
                                          activebackground='#6AFFD6',
                                          bg='#2286FF',
                                          pady=10, padx=20)
        play_again_button_no = tk.Button(windowTwo, text=" No ", command = dont_play_again,
                                         font=("MALDINI", 15),
                                         activebackground='#6AFFD6',
                                         bg='#2286FF',
                                         pady=10, padx=20)
        play_again_button_yes.place(x=650, y=580)
        play_again_button_no.place(x=800, y=580)


    if options.get()!="Selected":
     action = tk.Label(windowTwo ,font=("MALDINI", 15),
                       activebackground='#6AFFD6',
                       bg='#3D84B8',
                       text=f"\nYou chose {options.get()}, computer chose {computer_action}.\n")
     action.place(x=600, y=120)
     result3 = tk.Label(windowTwo, font=("MALDINI", 15),
                        activebackground='#6AFFD6',
                        bg='#3D84B8',
                        text=f"Your Score  {user_score}  :  Computer Score {computer_score} ")
     result3.place(x=640, y=0)
     show_button.destroy()
     again_button = tk.Button(windowTwo, text="Next Round",command=dest,
                              activebackground='#6AFFD6',
                              bg='#2286FF',
                              font=('MALDINI', 15),
                              pady=10, padx=20)
     again_button.place(x=690, y=420)

def back_window() :
    windowTwo.destroy()
    import home_page


back_button = tk.Button(windowTwo, text = "Back ",
                        activebackground='#6AFFD6',
                        bg='#2286FF',
                        font = ('MALDINI', 15),
                        command = back_window)

back_button.place(x = 0, y = 0)

options = tk.StringVar(windowTwo)
options.set("Selected")

user_action =tk.OptionMenu(windowTwo, options, "rock","paper", "scissors")
user_action.place(x=730, y=370)

please_input = tk.Label(windowTwo, text="Please Enter You Choice",
                        font=("MALDINI", 15),
                        activebackground='#6AFFD6',
                        bg='#3D84B8',
                        )

please_input.place(x=670, y=320)

show_button = tk.Button(windowTwo,text = " Go ", command= go,
                        activebackground='#2286FF',bg='#2286FF',
                        font=('MALDINI', 15),
                        pady = 10, padx = 20)

show_button.place(x=900, y=360)


window.mainloop()