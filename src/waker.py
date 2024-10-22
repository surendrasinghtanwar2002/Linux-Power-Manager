#!/home/lokendar/Program/waker_linux/.venv/bin/python3

import cv2
import time
import os
from face import Face

def notify(title):
    """Display a notification on Ubuntu."""
    os.system(f'notify-send "{title}"')

cap = cv2.VideoCapture(0)
face_detector = Face()

screen_off = False
flag = False
os.system("gsettings set org.gnome.desktop.session idle-delay 0")
last_face_time = time.time()


while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Check if there's any face in the frameos.system("xset s off")
    if face_detector.detected(frame=frame):
        last_face_time = time.time()
        face_detected = True
        flag = False

        if screen_off == True and face_detected == True:
            print("Face detected. Waking up computer...")
            os.system("gsettings set org.gnome.desktop.session idle-delay 0")
            # time.sleep(4)
            screen_off = False

    else:
        face_detected = False

    if not face_detected and time.time() - last_face_time > 5 and screen_off == False:
        # print("No face detected for 60 seconds. Minimizing windows and putting computer to sleep...")

        if not flag:
            notify('computer is about to sleep in 15 seconds')
            flag = True
        # time.sleep(10)

        if not face_detected and time.time() - last_face_time > 15 and screen_off == False:

            screen_off = True
            os.system("gsettings set org.gnome.desktop.session idle-delay 300")
            os.system("systemctl suspend -i")

    os.system("gsettings set org.gnome.desktop.session idle-delay 300")
    # cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


os.system("gsettings set org.gnome.desktop.session idle-delay 300")
cap.release()
cv2.destroyAllWindows()
