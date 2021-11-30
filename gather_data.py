import os
import cv2
import numpy as np

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Dense,Dropout,GlobalAveragePooling2D,Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from scipy import stats as st


def gather_data(num_samples):
    global lizard, spock, rock, paper, scissor, nothing

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

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

            roi = frame[5: box_size - 5, width - box_size + 5: width - 5]

            eval(class_name).append([roi, class_name])

            counter += 1

            text = "Collected Samples of {}: {}".format(class_name, counter)

        else:
            text = "Press 'r' to collect rock samples, 'p' for paper"
            text1 = "s' for scissor, 'l' for lizard, 'k' for spock,  and 'n' for nothing"
        cv2.putText(frame, text, (100, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame, text1, (100, 370), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255), 1, cv2.LINE_AA)

        cv2.imshow("Collecting images", frame)

        k = cv2.waitKey(1)

        if k == ord('r'):
            trigger = not trigger
            class_name = 'rock'
            rock = []

        if k == ord('p'):
            trigger = not trigger
            class_name = 'paper'
            paper = []

        if k == ord('s'):
            trigger = not trigger
            class_name = 'scissor'
            scissor = []


        if k == ord('l'):
            trigger = not trigger
            class_name = 'lizard'
            lizard = []

        if k == ord('k'):
            trigger = not trigger
            class_name = 'spock'
            spock = []

        if k == ord('n'):
            trigger = not trigger
            class_name = 'nothing'
            nothing = []

        # Exit if user presses 'q'
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
gather_data(100)

labels = [tupl[1] for tupl in rock] + [tupl[1] for tupl in paper] + [tupl[1] for tupl in scissor] + [tupl[1] for tupl in lizard] + [tupl[1] for tupl in spock] +[tupl[1] for tupl in nothing]

images = [tupl[0] for tupl in rock] + [tupl[0] for tupl in paper] + [tupl[0] for tupl in scissor] + [tupl[0] for tupl in lizard] + [tupl[0] for tupl in spock]+[tupl[0] for tupl in nothing]

images = np.array(images, dtype="float") / 255.0


encoder = LabelEncoder()

Int_labels = encoder.fit_transform(labels)

one_hot_labels = to_categorical(Int_labels, 6)

(trainX, testX, trainY, testY) = train_test_split(images, one_hot_labels, test_size=0.25, random_state=50)

images = []

image_size = 224

N_mobile = tf.keras.applications.NASNetMobile(input_shape=(image_size, image_size, 3), include_top=False,
                                              weights='imagenet')

N_mobile.trainable = False

x = N_mobile.output

x = GlobalAveragePooling2D()(x)

x = Dense(712, activation='relu')(x)

x = Dropout(0.40)(x)

preds = Dense(6, activation='softmax')(x)

model = Model(inputs=N_mobile.input, outputs=preds)


augment = ImageDataGenerator(

    rotation_range=30,
    zoom_range=0.25,
    width_shift_range=0.10,
    height_shift_range=0.10,
    shear_range=0.10,
    horizontal_flip=False,
    fill_mode="nearest"
)

model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

epochs = 20
batchsize = 25

history = model.fit(x=augment.flow(trainX, trainY, batch_size=batchsize), validation_data=(testX, testY),
steps_per_epoch= len(trainX) // batchsize, epochs=epochs)


model.save("rpslk4.h5", overwrite=True)


