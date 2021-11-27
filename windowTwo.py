import random
from tkinter.ttk import *
from PIL import ImageTk, Image

import tkinter as tk

windowTwo = tk.Tk()
windowTwo.geometry("1900x770")
windowTwo.title("Page 2")


bg1 = tk.PhotoImage(file = "sec1.png")
image_label = Label(windowTwo, image = bg1)
image_label.place(x = -2, y = -2, relwidth = 1, relheight = 1)


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

    if user_action.get() == computer_action:
        global result
        result=tk.Label(windowTwo, text=f"Both players selected {user_action.get()}. It's a tie!")
        result.place(x=150, y=140)
    elif user_action.get() == "rock":
        if computer_action == "scissors":
            user_score+=1
            result=tk.Label(windowTwo, text="Rock smashes scissors! You win!")
            result.place(x=150, y=140)

        else:
            computer_score += 1
            result=tk.Label(windowTwo, text="Paper covers rock! You lose.")

            result.place(x=150, y=140)

    elif user_action.get() == "paper":
        if computer_action == "rock":
            result=tk.Label(windowTwo, text="Paper covers rock! You win!")
            user_score += 1
            result.place(x=150, y=140)
        else:
            computer_score += 1
            result=tk.Label(windowTwo, text="Scissors cuts paper! You lose.")
            result.place(x=150, y=140)
    elif user_action.get() == "scissors":
        if computer_action == "paper":
            result=tk.Label(windowTwo, text="Scissors cuts paper! You win!")
            user_score += 1
            result.place(x=150, y=140)

        else :
            computer_score += 1
            result=tk.Label(windowTwo, text="Rock smashes scissors! You lose.")
            result.place(x=150, y=140)

    # show_button.destroy()
    if user_score == 1 or computer_score == 1 :
        result4 = tk.Label(windowTwo, text="Game Finished Wanna play again?")
        result4.place(x=150, y=280)
        def play_again() :
            dest()
            play_again_button_yes.destroy()
            play_again_button_no.destroy()
            result3.destroy()
            global user_score
            user_score = 0
            global computer_score
            computer_score = 0
            result4.destroy()
        play_again_button_yes = tk.Button(windowTwo, text="Yes", command = play_again, activeforeground="red", activebackground="blue",pady=10, padx=20)
        play_again_button_no = tk.Button(windowTwo, text="No", command = dont_play_again, activeforeground="red", activebackground="blue",pady=10, padx=20)
        play_again_button_yes.place(x=400, y=250)
        play_again_button_no.place(x=500, y=250)
    def dest():
     global show_button
     global result
     result.destroy()
     action.destroy()
     user_action.delete(0, 10)
     show_button = tk.Button(windowTwo, text="Go", command=go, activeforeground="red", activebackground="blue", pady=10,padx=20)
     show_button.place(x=400, y=200)

    if user_action.get():
     action = tk.Label(windowTwo, text=f"\nYou chose {user_action.get()}, computer chose {computer_action}.\n")
     action.place(x=150, y=80)
     result3 = tk.Label(windowTwo,text=f"The total  score is {user_score} For You and  {computer_score} for Computer")
     result3.place(x=150, y=260)
     show_button.destroy()
     again_button = tk.Button(windowTwo, text="Next Round",command=dest, activeforeground="red", activebackground="blue",pady=10, padx=20)
     again_button.place(x=0, y=0)

user_action = tk.Entry(windowTwo,borderwidth=5)
user_action.place(x=190, y=200)
name_label = tk.Label(windowTwo, text="Choice").place(x=150, y=200)
please_input = tk.Label(windowTwo, text="Please Enter You Choice").place(x=180, y=180)

show_button = tk.Button(windowTwo,text = "Go", command= go, activeforeground = "red",activebackground = "blue",pady=10,padx=20)

show_button.place(x=400, y=200)
