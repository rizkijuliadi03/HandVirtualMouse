import cv2
import mediapipe as mp
import pyautogui
from mediapipe.python.solutions import drawing_utils

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
screen_width, screen_height = pyautogui.size()
index_y = 0
thumb_y = 0
middle_y = 0
ring_y = 0
little_y = 0

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            # Mengakses landmark dari hand
            for id, landmark in enumerate(hand.landmark):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)

                #Jari Telunjuk
                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 0))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x, index_y, duration=0)

                #Jari Jempol
                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 0))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y

                # Jari Tengah
                if id == 12:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 0))
                    middle_x = screen_width / frame_width * x
                    middle_y = screen_height / frame_height * y
                    if abs(middle_y - thumb_y) < 10:
                        pyautogui.click()
                        pyautogui.sleep(1)
                        print('click')

                # Jari Manis
                if id == 16:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 0))
                    ring_x = screen_width / frame_width * x
                    ring_y = screen_height / frame_height * y
                    if abs(ring_y - thumb_y) < 10:
                        pyautogui.rightClick()
                        pyautogui.sleep(1)
                        print('Right click')

                # Jari Kelingking
                if id == 20:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 0))
                    little_x = screen_width / frame_width * x
                    little_y = screen_height / frame_height * y
                    if abs(little_y - thumb_y) < 10:
                        pyautogui.click()
                        pyautogui.sleep(1)
                        print('Scroll')

    cv2.imshow('Virtual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Tekan 'Esc' untuk keluar
        break

cap.release()
cv2.destroyAllWindows()