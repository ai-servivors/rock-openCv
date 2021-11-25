"""
import random
from enum import IntEnum


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

class RockPaperScissors:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

    @staticmethod
    def get_user_selection():
        choices = [f"{action.name}[{action.value}]" for action in Action]
        choices_str = ", ".join(choices)
        selection = int(input(f"Enter a choice ({choices_str}): "))
        action = Action(selection)
        return action

    @staticmethod
    def get_computer_selection():
        selection = random.randint(0, len(Action) - 1)
        action = Action(selection)
        return action

    def play(self):
        while True:
            try:
                user_action = self.get_user_selection()
            except ValueError as e:
                range_str = f"[0, {len(Action) - 1}]"
                print(f"Invalid selection. Enter a value in range {range_str}")
                continue

            computer_action = self.get_computer_selection()
            self.track_winner(user_action, computer_action)
            if self.determine_winner(self.user_score,self.computer_score):
                play_again = input("Play again? (y/n): ")
                if play_again.lower() != "y":
                    break

    def reset_scores(self):
        self.user_score = 0
        self.computer_score = 0

    def determine_winner(self, user_score, computer_score ):
        if user_score == 3 or computer_score == 3:
            if user_score == 3:
                print("Congratulation.. You are the Winner")
            else:
                print("Unfortunately.. The computer beats you..")
            self.reset_scores()
            return True
        return False


    def track_winner(self, user_action, computer_action):
        if user_action == computer_action:
            print(f"Both players selected {user_action.name}. It's a tie!")
            print(f"Your total points is {self.user_score} and computer total points is {self.computer_score}")
        elif user_action == Action.Rock:
            if computer_action == Action.Scissors:
                self.user_score += 1
                print(f"Rock smashes scissors! You win extra point! ")
                print(f"Your total points is {self.user_score} and computer total points is {self.computer_score}")
            else:
                self.computer_score += 1
                print("Paper covers rock! You don't make any advance.")
                print(f"Your total points is {self.user_score} and computer total points is {self.computer_score}")
        elif user_action == Action.Paper:
            if computer_action == Action.Rock:
                self.user_score += 1
                print("Paper covers rock! You win extra point!")
                print(f"Your total points is {self.user_score} and computer total points is {self.computer_score}")
            else:
                self.computer_score += 1
                print("Scissors cuts paper! You don't make any advance.")
                print(f"Your total points is {self.user_score} and computer total points is {self.computer_score}")
        elif user_action == Action.Scissors:
            if computer_action == Action.Paper:
                self.user_score += 1
                print("Scissors cuts paper! You win extra point!")
                print(f"Your total points is {self.user_score} and computer total points is {self.computer_score}")
            else:
                self.computer_score += 1
                print("Rock smashes scissors! You don't make any advance.")
                print(f"Your total points is {self.user_score} and computer total points is {self.computer_score}")




if __name__ == "__main__":
    rock_paper_scissors = RockPaperScissors()
    rock_paper_scissors.play()
    print('test')
"""
import random
from enum import IntEnum

import tkinter as tk
windowTwo = tk.Tk()
windowTwo.geometry("400x250")
windowTwo.title("Page 22222")

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

class RockPaperScissors:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

#    @staticmethod
def get_user_selection():
    global selection
    choices = "Rock [0] , Paper [1] , Scissors [2] : "
    label_message_selecion = tk.Label(text=f"Enter a choice {choices}")
    label_message_selecion.pack()
    selection = tk.Entry(windowTwo)
    selection.place(x=190, y=140)

def get_computer_selection():
    Computer_selection = random.randint(0, 1)
    return Computer_selection

def play ():
    print (get_computer_selection())
    print (selection.get())

    global label_message_selecion
    if int(selection.get()) < 3 and int(selection.get()) >= 0 :
        comparasion()
        show_button.destroy()
        #label_message_selecion.destroy()
    else :
        label_message_selecion = tk.Label(text="Invalid selection Enter a value in range")
        label_message_selecion.pack()
def names(num) :
    if num == 1 :
        return 'Paper'
    if num == 2 :
        return 'Scissors'
    if num == 0 :
        return 'Rock'

def comparasion():
    computerSelection = get_computer_selection()
    global computer_score
    global player_Score
    computer_score = 0
    player_Score = 0

    if int(selection.get()) == computerSelection :
        label_message_s = tk.Label(text=f'Both players selected {selection.get()} . Its a tie!')
        label_message_s.pack()
        redo_button = tk.Button(windowTwo, text="Go", command=play, activeforeground="red", activebackground="blue",pady=10, padx=20)
        redo_button.place(x=300, y=250)

    else :
        label_message_comp = tk.Label(text=f'Computer selected : {names(computerSelection)}')
        label_message_comp.pack()
        label_message_sel = tk.Label(text=f'You Select selected : {names(int(selection.get()))}')
        label_message_sel.pack()
        redo_button = tk.Button(windowTwo, text="Go", command=play, activeforeground="red", activebackground="blue",pady=10, padx=20)
        redo_button.place(x=300, y=250)
    if int(selection.get()) < 1 and computerSelection == 1 :

        computer_score += 1
        label_message_comp = tk.Label(text=f'Computer Score : {computer_score}')
        label_message_comp.place(x = 150,y = 140)
        label_message_comp = tk.Label(text=f'Your Score : {player_Score}')
        label_message_comp.place(x = 150,y = 160)
        redo_button = tk.Button(windowTwo, text="Go", command=play, activeforeground="red", activebackground="blue",pady=10, padx=20)
        redo_button.place(x=300, y=250)


    if int(selection.get()) > 1 and computerSelection == 1 :
        player_Score += 1
        label_message_comp = tk.Label(text=f'Computer Score : {computer_score}')
        label_message_comp.pack()
        label_message_comp = tk.Label(text=f'Your Score : {player_Score}')
        label_message_comp.pack()
        redo_button = tk.Button(windowTwo, text="Go", command=play, activeforeground="red", activebackground="blue",pady=10, padx=20)
        redo_button.place(x=300, y=250)

show_button = tk.Button(windowTwo,text = "Go", command= play, activeforeground = "red",activebackground = "blue",pady=10,padx=20)
show_button.place(x = 300, y = 200)

get_user_selection()
