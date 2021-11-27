import cv2
import numpy as np
from tensorflow.keras.utils import to_categorical

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def gather_data(num_samples):

    global rock, paper, scissor, nothing

    cap = cv2.VideoCapture(0,  cv2.CAP_DSHOW)
    trigger = False
    counter = 0
    box_size = 234
    width = int(cap.get(3))

    while True:

        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        if not ret:
            break

        if counter == num_samples:
            trigger = not trigger
            counter = 0

        cv2.rectangle(frame, (width - box_size, 0), (width, box_size), (0, 250, 150), 2)
        cv2.namedWindow("Collecting images", cv2.WINDOW_NORMAL)

        if trigger:
            roi = frame[5: box_size-5 , width-box_size + 5: width -5]
            eval(class_name).append([roi, class_name])
            counter += 1
            text = "Collected Samples of {}: {}".format(class_name, counter)

        else:
            text = "Press 'r' to collect rock samples, 'p' for paper, 's' for scissor and 'n' for nothing"

        cv2.putText(frame, text, (3, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.imshow("Collecting images", frame)
        choice = cv2.waitKey(1)

        if choice == ord('r'):
            trigger = not trigger
            class_name = 'rock'
            rock = []

        if choice == ord('p'):
            trigger = not trigger
            class_name = 'paper'
            paper = []

        if choice == ord('s'):
            trigger = not trigger
            class_name = 'scissor'
            scissor = []

        if choice == ord('n'):
            trigger = not trigger
            class_name = 'nothing'
            nothing = []

        if choice == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

gather_data(100)


labels = [tupl[1] for tupl in rock] + [tupl[1] for tupl in paper] + [tupl[1] for tupl in scissor] +[tupl[1] for tupl in nothing]
images = [tupl[0] for tupl in rock] + [tupl[0] for tupl in paper] + [tupl[0] for tupl in scissor] +[tupl[0] for tupl in nothing]
images = np.array(images, dtype="float") / 255.0
print('Total images: {} , Total Labels: {}'.format(len(labels), len(images)))
encoder = LabelEncoder()
Int_labels = encoder.fit_transform(labels)
one_hot_labels = to_categorical(Int_labels, 4)
(trainX, testX, trainY, testY) = train_test_split(images, one_hot_labels, test_size=0.25, random_state=50)
images = []
