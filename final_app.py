import cv2
import numpy as np
import time
from tensorflow.keras.models import Model, load_model
from playsound import playsound
from random import choice,shuffle
from scipy import stats as st

from collections import deque

model = load_model("rpslk4.h5")

def findout_winner(user_move, Computer_move):

    if user_move == Computer_move:
        return "Tie"

    elif user_move == "rock" and Computer_move == "scissor":
        return "User"
    elif user_move == "rock" and Computer_move == "lizard":
        return "User"
    elif user_move == "rock" and Computer_move == "paper":
        return "Computer"
    elif user_move == "rock" and Computer_move == "spock":
        return "Computer"

    elif user_move == "scissor" and Computer_move == "paper":
        return "User"
    elif user_move == "scissor" and Computer_move == "lizard":
        return "User"
    elif user_move == "scissor" and Computer_move == "rock":
        return "Computer"
    elif user_move == "scissor" and Computer_move == "spock":
        return "Computer"


    elif user_move == "paper" and Computer_move == "rock":
        return "User"
    elif user_move == "paper" and Computer_move == "spock":
        return "User"
    elif user_move == "paper" and Computer_move == "scissor":
        return "Computer"
    elif user_move == "paper" and Computer_move == "lizard":
        return "Computer"

    elif user_move == "lizard" and Computer_move == "spock":
        return "User"
    elif user_move == "lizard" and Computer_move == "paper":
        return "User"
    elif user_move == "lizard" and Computer_move == "scissor":
        return "Computer"
    elif user_move == "lizard" and Computer_move == "rock":
        return "Computer"

    elif user_move == "spock" and Computer_move == "rock":
        return "User"
    elif user_move == "spock" and Computer_move == "scissor":
        return "User"
    elif user_move == "spock" and Computer_move == "lizard":
        return "Computer"
    elif user_move == "spock" and Computer_move == "paper":
        return "Computer"


def show_winner(user_socre, computer_score):

    if user_socre > computer_score:
        playsound('sounds/win.mp3', block=False)
        img = cv2.imread("images/youwin.png")

    elif user_socre < computer_score:
        playsound('sounds/lost.mp3', block=False)
        img = cv2.imread("images/youlose.png")

    else:
        img = cv2.imread("images/draw.jpg")

    cv2.putText(img, "Press 'ENTER' to play again, else exit",
                (100, 600), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow("Rock Paper Scissors", img)

    k = cv2.waitKey(0)

    if k == 13:
        return True

    else:
        return False

def display_computer_move(computer_move_name, frame):
    icon = cv2.imread("images/{}.png".format(computer_move_name))
    icon = cv2.resize(icon, (224, 224))

    roi = frame[0:224, 0:224]

    mask = icon[:, :, -1]

    mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)[1]

    icon_bgr = icon[:, :, :3]

    img1_bg = cv2.bitwise_and(roi, roi, mask=cv2.bitwise_not(mask))

    img2_fg = cv2.bitwise_and(icon_bgr, icon_bgr, mask=mask)

    combined = cv2.add(img1_bg, img2_fg)

    frame[0:224, 0:224] = combined

    return frame

cap = cv2.VideoCapture(0)

box_size = 234
width = int(cap.get(3))

computer_move_name = "nothing"
final_user_move = "nothing"

label_names = ['lizard', 'nothing', 'paper', 'rock', 'scissor', 'spock']

computer_score, user_score = 0, 0

rect_color = (255, 0, 0)

hand_inside = False

confidence_threshold = 0.70

smooth_factor = 5

de = deque(['nothing'] * 5, maxlen=smooth_factor)
wait=False
start_time = time.time()
while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    cv2.namedWindow("Rock Paper Scissors", cv2.WINDOW_NORMAL)

    roi = frame[5: box_size - 5, width - box_size + 5: width - 5]

    roi = np.array([roi]).astype('float64') / 255.0

    pred = model.predict(roi)

    move_code = np.argmax(pred[0])

    user_move = label_names[move_code]

    prob = np.max(pred[0])

    if prob >= confidence_threshold:

        de.appendleft(user_move)

        try:
            final_user_move = st.mode(de)[0][0]

        except StatisticsError:
            print('Stats error')
            continue

        if final_user_move != "nothing" and hand_inside == False:

            hand_inside = True

            computer_move_name = choice(['lizard', 'paper', 'rock', 'scissor', 'spock'])
            winner = findout_winner(final_user_move, computer_move_name)
            display_computer_move(computer_move_name, frame)

            if winner == "Computer":
                computer_score += 1
                rect_color = (0, 0, 255)
                playsound('sounds/lost1.wav', block=False)
            elif winner == "User":
                playsound('sounds/win1.mp3', block=False)
                user_score += 1
                rect_color = (0, 250, 0)

            elif winner == "Tie":
                rect_color = (255, 250, 255)

            if user_score == 5 or computer_score== 5 :


                if not wait:

                    start_time = time.time()
                wait = True

        if (time.time() - start_time) > 3 and (user_score == 5 or computer_score== 5):

            play_again = show_winner(user_score, computer_score)

            if play_again:
                user_score, computer_score = 0, 0
            else:
                break

        elif final_user_move != "nothing" and hand_inside == True:

            display_computer_move(computer_move_name, frame)
        elif final_user_move == 'nothing':
            hand_inside = False
            rect_color = (255, 0, 0)
    cv2.putText(frame, "Your Move: " + final_user_move,
                (420, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.putText(frame, "Computer's Move: " + computer_move_name,
                (2, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.putText(frame, "Your Score: " + str(user_score),
                (420, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(frame, "Computer Score: " + str(computer_score),
                (2, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.putText(frame, "Get 5 Points To Win!", (160, 400), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                (255, 255, 255), 1, cv2.LINE_AA)

    cv2.rectangle(frame, (width - box_size, 0), (width, box_size), rect_color, 2)

    cv2.imshow("Rock Paper Scissors", frame)

    k = cv2.waitKey(10)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()