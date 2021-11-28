import random
import tkinter as tk

windowTwo = tk.Tk()
windowTwo.geometry("1920x1080")
windowTwo.title("Page 2")

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
        result=tk.Label(windowTwo,font=("Arial", 16), text=f"Opps!! Both players selected {options.get()}. It's a tie!")
        result.place(x=650, y=210)
    elif options.get() == "rock":
        if computer_action == "scissors":
            user_score+=1
            result=tk.Label(windowTwo,font=("Arial", 16), text="Rock smashes scissors! You win!")
            result.place(x=650, y=210)

        else:
            computer_score += 1
            result=tk.Label(windowTwo,font=("Arial", 16), text="Paper covers rock! You lose.")

            result.place(x=650, y=210)

    elif options.get() == "paper":
        if computer_action == "rock":
            result=tk.Label(windowTwo,font=("Arial", 16), text="Paper covers rock! You win!")
            user_score += 1
            result.place(x=650, y=210)
        else:
            computer_score += 1
            result=tk.Label(windowTwo,font=("Arial", 16), text="Scissors cuts paper! You lose.")
            result.place(x=650, y=210)
    elif options.get() == "scissors":
        if computer_action == "paper":
            result=tk.Label(windowTwo,font=("Arial", 16), text="Scissors cuts paper! You win!")
            user_score += 1
            result.place(x=650, y=210)

        else :
            computer_score += 1
            result=tk.Label(windowTwo,font=("Arial", 16), text="Rock smashes scissors! You lose.")
            result.place(x=650, y=210)

    # show_button.destroy()
    if user_score == 5 or computer_score == 5 :
        result4 = tk.Label(windowTwo,font=("Arial", 29), text="Game Finished Wanna play again?")
        result4.place(x=470, y=500)
        def play_again() :
            # result7 = tk.Label(windowTwo,text="", pady=20, padx=80)
            # result7.place(x=700, y=410)
            # again_button.destroy()
            dest()
            again_button.destroy()
            play_again_button_yes.destroy()
            play_again_button_no.destroy()

            global user_score
            user_score = 0
            global computer_score
            computer_score = 0
            result4.destroy()
            result3 = tk.Label(windowTwo, font=("Arial", 14),text=f"Your Score  {user_score}  :  Computer Score {computer_score} ")
            result3.place(x=640, y=0)

        play_again_button_yes = tk.Button(windowTwo, text="Yes", command = play_again, activeforeground="red", activebackground="blue",pady=10, padx=20)
        play_again_button_no = tk.Button(windowTwo, text="No", command = dont_play_again, activeforeground="red", activebackground="blue",pady=10, padx=20)
        play_again_button_yes.place(x=650, y=580)
        play_again_button_no.place(x=800, y=580)
    def dest():
     again_button.destroy()
     global show_button
     global result
     result.destroy()
     action.destroy()
     # user_action.delete(0, 10)
     show_button = tk.Button(windowTwo, text="Go", command=go, activeforeground="red", activebackground="blue", pady=10,padx=20)
     show_button.place(x=900, y=340)

    if options.get()!="Selected":
     action = tk.Label(windowTwo ,font=("Arial", 18), text=f"\nYou chose {options.get()}, computer chose {computer_action}.\n")
     action.place(x=560, y=120)
     result3 = tk.Label(windowTwo, font=("Arial", 14),text=f"Your Score  {user_score}  :  Computer Score {computer_score} ")
     result3.place(x=640, y=0)
     show_button.destroy()
     again_button = tk.Button(windowTwo, text="Next Round",command=dest, activeforeground="red", activebackground="blue",pady=10, padx=20)
     again_button.place(x=700, y=410)




options = tk.StringVar(windowTwo)
options.set("Selected") # default value

user_action =tk.OptionMenu(windowTwo, options, "rock","paper", "scissors")
user_action.place(x=730, y=350)
#
# user_action = tk.Entry(windowTwo,borderwidth=5)
# user_action.place(x=730, y=350)
# name_label = tk.Label(windowTwo, text="Choice").place(x=680, y=350)
please_input = tk.Label(windowTwo, text="Please Enter You Choice").place(x=710, y=320)

show_button = tk.Button(windowTwo,text = "Go", command= go, activeforeground = "red",activebackground = "blue",pady=10,padx=20)

show_button.place(x=900, y=340)
