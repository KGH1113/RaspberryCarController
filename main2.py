import cv2
import mediapipe as mp
from HandStatus import *
from BluetoothControl import *
control = ScreenControling()

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
CarStatus = None

with mp_hands.Hands(model_complexity=1, min_detection_confidence=0.8, min_tracking_confidence=0.8) as hands:
    tracking = Tracking(mp_drawing, mp_drawing_styles, mp_hands, hands, False)
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignored camera frame!")
            continue
        
        image, results = tracking.process(image)
        image_height, image_width, _ = image.shape

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                finger_status = tracking.get_fingers_status(image, image_height, hand_landmarks, results, draw=True)
                hand_pos = tracking.get_hand_pos(hand_landmarks)
            hand_lr = tracking.get_hand_lr(results)

            if hand_lr == 'Right':
                if finger_status['index'] == 0 and finger_status['middle'] == 0 and finger_status['ring'] == 0 and finger_status['pinky'] == 0:
                    if hand_pos.x < 0.5:
                        control.click_left()
                        if CarStatus == 'turning_left':
                            continue
                        CarStatus = 'turning_left'
                        print(CarStatus)
                    if hand_pos.x > 0.5:
                        control.click_right()
                        if CarStatus == 'turning_right':
                            continue
                        CarStatus = 'turning_right'
                        print(CarStatus)
                    if hand_pos.z > 0.5:
                        control.click_go()
                        if CarStatus == 'going_front':
                            continue
                        CarStatus = 'going_front'
                        print(CarStatus)
                    if hand_pos.z < 0.5:
                        control.click_back()
                        if CarStatus == 'going_back':
                            continue
                        CarStatus = 'going_back'
                        print(CarStatus)

        cv2.imshow('Car Controling', cv2.flip(image, 1))
        # Flip the image horizontally for a selfie-view display.
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()