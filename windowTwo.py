import random
import tkinter as tk
from tkinter.ttk import *
from playsound import playsound
windowTwo = tk.Tk()
windowTwo.geometry("1920x1080")
windowTwo.title("Page 2")
bg = tk.PhotoImage(file = "assets/secondpage.png")
image_label = Label(windowTwo, image = bg)
image_label.place(x = -2, y = -2)

user_score = 0
computer_score = 0
#################################
############ OPTION #############
options = tk.StringVar(windowTwo)
options.set("Selected")
user_action = tk.OptionMenu(windowTwo, options, "rock", "paper", "scissors","lizard","spock")
user_action.place(x = 730, y = 370)
please_input = tk.Label(windowTwo, text = "Please Enter You Choice",
                        font = ("MALDINI", 15),
                        activebackground = '#6AFFD6',
                        bg = '#2fa0e4')
please_input.place(x = 670, y = 320)
####################################
########### No Function ############
def dont_play_again():
    windowTwo.destroy()
    import home_page
###########################
########## DEST ###########
def dest():
        global show_button
        global result
        result.destroy()
        action.destroy()
        again_button.destroy()
        show_button = tk.Button(windowTwo, text=" Go ", command = go,
                                activebackground='#6AFFD6',
                                bg='#2286FF',
                                font=('MALDINI', 15),
                                pady=10, padx=20)
        show_button.place(x=900, y=360)
##################################
############ GO FUNC #############
def go() :
    global action, user_score, computer_score
    possible_actions = ["rock", "paper", "scissors","lizard","spock"]
    computer_action = random.choice(possible_actions)
    action = tk.Label(windowTwo, font=("MALDINI", 15),
                      activebackground='#6AFFD6',
                      bg='#2fa0e4',
                      text=f"\nYou chose {options.get()}, computer chose {computer_action}.\n")
    action.place(x=600, y=120)
    #####################################
    ############ GAME LOGIC #############
    if options.get() == computer_action :
        computer_action = random.choice(possible_actions)
        global result
        result = tk.Label(windowTwo, font=("MALDINI", 15),
                          activebackground='#6AFFD6',
                          bg='#2fa0e4',
                          text=f" Opps!! Both players selected {options.get()}. It's a tie! ")
        result.place(x=650, y=210)
    elif options.get() == "rock":
        if computer_action == "scissors":
            user_score += 1
            result = tk.Label(windowTwo, font=("MALDINI", 15),
                              activebackground='#6AFFD6',
                              bg='#2fa0e4',
                              text="Rock smashes scissors! You win!")
            result.place(x=650, y=210)
            playsound('sounds/win1.mp3', block=False)
        elif computer_action == "lizard":
            user_score += 1
            result = tk.Label(windowTwo, font=("MALDINI", 15),
                              activebackground='#6AFFD6',
                              bg='#2fa0e4',
                              text="Rock smashes lizard! You win!")
            result.place(x=650, y=210)
            playsound('sounds/win1.mp3', block=False)
        elif computer_action == "spock":
            computer_score += 1
            result = tk.Label(windowTwo, font=("MALDINI", 15),
                              activebackground='#6AFFD6',
                              bg='#2fa0e4',
                              text=" spock covers rock! You lose. ")
            result.place(x=650, y=210)
            playsound('sounds/lost1.wav', block=False)

        else:
               computer_score += 1
               result = tk.Label(windowTwo, font=("MALDINI", 15),
                          activebackground='#6AFFD6',
                          bg='#2fa0e4',
                          text=" Paper covers rock! You lose. ")
               result.place(x=650, y=210)
               playsound('sounds/lost1.wav', block=False)


    elif options.get() == "paper":
        if computer_action == "rock":
            result = tk.Label(windowTwo, font=("MALDINI", 15),
                              activebackground='#6AFFD6',
                              bg='#2fa0e4',
                              text=" Paper covers rock! You win! ")
            user_score += 1
            result.place(x=650, y=210)
            playsound('sounds/win1.mp3', block=False)
        elif computer_action == "spock":
            result = tk.Label(windowTwo, font=("MALDINI", 15),
                              activebackground='#6AFFD6',
                              bg='#2fa0e4',
                              text=" Paper covers spock! You win! ")
            user_score += 1
            result.place(x=650, y=210)
            playsound('sounds/win1.mp3', block=False)
        elif computer_action == "lizard":
            computer_score += 1
            result = tk.Label(windowTwo, font = ("MALDINI", 15),
                              activebackground='#6AFFD6',
                              bg='#2fa0e4',
                              text=" lizard eats paper! You lose. ")
            result.place(x=650, y=210)
            playsound('sounds/lost1.wav', block=False)

        else:
            computer_score += 1
            result = tk.Label(windowTwo, font=("MALDINI", 15),
                          activebackground='#6AFFD6',
                          bg='#2fa0e4',
                          text=" Scissors cuts paper! You lose. ")
            result.place(x=650, y=210)
            playsound('sounds/lost1.wav', block=False)
    elif options.get() == "scissors":
        if computer_action == "paper":
            result = tk.Label(windowTwo, font = ("MALDINI", 15),
                              activebackground = '#6AFFD6',
                              bg = '#2fa0e4',
                              text = " Scissors cuts paper! You win! ")
            user_score += 1
            result.place(x=650, y=210)
            playsound('sounds/win1.mp3', block=False)
        elif computer_action == "lizard":
            result = tk.Label(windowTwo, font=("MALDINI", 15),
                              activebackground='#6AFFD6',
                              bg='#2fa0e4',
                              text=" Scissors cuts lizard! You win! ")
            user_score += 1
            result.place(x=650, y=210)
            playsound('sounds/win1.mp3', block=False)
        elif computer_action == "spock":
            computer_score += 1
            result = tk.Label(windowTwo, font=("MALDINI", 15),
                              activebackground='#6AFFD6',
                              bg='#2fa0e4',
                              text=" spock smashes scissors! You lose. ")
            result.place(x=650, y=210)
            playsound('sounds/lost1.wav', block=False)
        else:
           computer_score += 1
           result = tk.Label(windowTwo, font=("MALDINI", 15),
                          activebackground='#6AFFD6',
                          bg='#2fa0e4',
                          text=" Rock smashes scissors! You lose. ")
           result.place(x=650, y=210)
           playsound('sounds/lost1.wav', block=False)


    elif options.get() == "spock":
        if computer_action == "rock":
            result = tk.Label(windowTwo, font=("MALDINI", 15),
                              activebackground='#6AFFD6',
                              bg='#2fa0e4',
                              text=" spock covers rock! You win! ")
            user_score += 1
            result.place(x=650, y=210)
            playsound('sounds/win1.mp3', block=False)
        elif computer_action == "scissors":
            result = tk.Label(windowTwo, font=("MALDINI", 15),
                              activebackground='#6AFFD6',
                              bg='#2fa0e4',
                              text=" spock smashes  scissors! You win! ")
            user_score += 1
            result.place(x=650, y=210)
            playsound('sounds/win1.mp3', block=False)
        elif computer_action == "paper":
            computer_score += 1
            result = tk.Label(windowTwo, font=("MALDINI", 15),
                              activebackground='#6AFFD6',
                              bg='#2fa0e4',
                              text=" paper covers spock! You lose. ")
            result.place(x=650, y=210)
            playsound('sounds/lost1.wav', block=False)

        else:
           computer_score += 1
           result = tk.Label(windowTwo, font=("MALDINI", 15),
                          activebackground='#6AFFD6',
                          bg='#2fa0e4',
                          text=" lizard eats spock! You lose. ")
           result.place(x=650, y=210)
           playsound('sounds/lost1.wav', block=False)

    elif options.get() == "lizard":
        if computer_action == "paper":
            result = tk.Label(windowTwo, font=("MALDINI", 15),
                              activebackground='#6AFFD6',
                              bg='#2fa0e4',
                              text=" lizard eats paper! You win! ")
            user_score += 1
            result.place(x=650, y=210)
            playsound('sounds/win1.mp3', block=False)
        elif computer_action == "spock":
            result = tk.Label(windowTwo, font=("MALDINI", 15),
                              activebackground='#6AFFD6',
                              bg='#2fa0e4',
                              text=" lizard eats spock! You win! ")
            user_score += 1
            result.place(x=650, y=210)
            playsound('sounds/win1.mp3', block=False)
        elif computer_action == "rock":
            computer_score += 1
            result = tk.Label(windowTwo, font=("MALDINI", 15),
                              activebackground='#6AFFD6',
                              bg='#2fa0e4',
                              text=" Rock smashes lizard! You lose. ")
            result.place(x=650, y=210)
            playsound('sounds/lost1.wav', block=False)
        else:
           computer_score += 1
           result = tk.Label(windowTwo, font=("MALDINI", 15),
                          activebackground='#6AFFD6',
                          bg='#2fa0e4',
                          text=" scissors cuts lizard! You lose. ")
           result.place(x=650, y=210)
           playsound('sounds/lost1.wav', block=False)
    ###########################
    ######## YES FUNC #########
    def play_again():
        play_again_button_yes.destroy()
        play_again_button_no.destroy()
        dest()
        global user_score
        user_score = 0
        global computer_score
        computer_score = 0
        result4.destroy()
        result3 = tk.Label(windowTwo, font=("MALDINI", 15),
                           activebackground='#6AFFD6',
                           bg='#2fa0e4',
                           text=f"  Your Score  {user_score}  :  Computer Score {computer_score}  ")
        result3.place(x=635, y=0)
    ############################
    ########## SELECT ##########
    if options.get() != "Selected" :

        result3 = tk.Label(windowTwo, font=("MALDINI", 15),
                            activebackground='#6AFFD6',
                            bg='#2fa0e4',
                            text=f"Your Score  {user_score}  :  Computer Score {computer_score} ")
        result3.place(x=640, y=0)
        show_button.destroy()
        global again_button
        again_button = tk.Button(windowTwo, text = "Next Round",command = dest,
                                  activebackground = '#6AFFD6',
                                  bg = '#2286FF',
                                  font = ('MALDINI', 15),
                                  pady = 10, padx = 20)
        again_button.place(x = 705, y = 420)
    ##############################
    ######## GAME FIINISH ########
    if user_score == 5 or computer_score == 5 :
        if user_score == 5:
           playsound('sounds/win.mp3', block=False)
        if computer_score == 5:
            playsound('sounds/lost.mp3', block=False)
        result4 = tk.Label(windowTwo, font=("MALDINI", 20),
                                activebackground='#6AFFD6',
                                bg='#2fa0e4',

                                text=" Game Finished Wanna play again? ")
        result4.place(x=550, y=500)
        global play_again_button_yes, play_again_button_no
        again_button.destroy()
        play_again_button_yes = tk.Button(windowTwo, text = " Yes ", command = play_again,
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
###############################
############ BACK #############
def back_window() :
    windowTwo.destroy()
    import home_page
back_button = tk.Button(windowTwo, text = "Back ",
                        activebackground='#6AFFD6',
                        bg='#2286FF',
                        font = ('MALDINI', 15),
                        command = back_window)
back_button.place(x = 5, y = 5)
#############################
############ GO #############
show_button = tk.Button(windowTwo,text = " Go ", command = go,
                        activebackground = '#2286FF',bg = '#2286FF',
                        font = ('MALDINI', 15),
                        pady = 10, padx = 20)
show_button.place(x = 900, y = 360)
window.mainloop()
