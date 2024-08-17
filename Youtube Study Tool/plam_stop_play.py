import cv2
import pyautogui
import mediapipe as mp
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Initialize video capture
cap = cv2.VideoCapture(0)

# Variables to manage detection and delay
detection_time = 0
delay = 3  # seconds
pressed = False
canPress = False

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Convert the BGR image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    # Draw hand annotations on the image
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Check if palm is open
            landmarks = hand_landmarks.landmark
            thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP].y
            pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP].y
            wrist = landmarks[mp_hands.HandLandmark.WRIST].y

            if thumb_tip < wrist and pinky_tip < wrist:
                # current_time = time.time()
                
                # # Perform the task if not already performed
                # if not pressed:
                #     pyautogui.press('space')
                #     print("Palm detected. Space key pressed.")
                #     detection_time = current_time
                #     pressed = True
                if not canPress:
                    pyautogui.press('space')
                    print("Palm detected. Space key pressed.")
                    canPress = True
    else:
        if canPress: 
            canPress = False
                
                

    # Check if delay has passed
    if pressed and (time.time() - detection_time) >= delay:
        pressed = False

    # Display the image
    cv2.imshow('Hand Tracking', image)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()  
