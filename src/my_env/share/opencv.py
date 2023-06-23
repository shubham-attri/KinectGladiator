import math

import mediapipe as mp
import keyboard
import cv2
import numpy as np
import pyautogui

pyautogui.FAILSAFE = False
screenWidth, screenHeight = pyautogui.size()
print("Screen width:", screenWidth)

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
mp_hands = mp.solutions.hands

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    # Flip the image horizontally for a selfie-view display.

    if results.pose_landmarks is not None:
        landmarks = results.pose_landmarks.landmark
        left_shoulder = landmarks[11]
        right_shoulder = landmarks[12]
        waist = landmarks[24]
        chest = landmarks[12]
        left_elbow = landmarks[13]
        right_elbow = landmarks[14]
        left_wrist = landmarks[15]
        right_wrist = landmarks[16]
        middle_finger = landmarks[20]
        left_knee = landmarks[25]
        right_knee = landmarks[26]
        left_middle_finger_tip = landmarks[19]
        right_middle_finger_tip = landmarks[20]

        #printing the above

        # Set initial y-coordinate offset
        y_offset = 70

        # Print left shoulder coordinates
        cv2.putText(image, f"Left Shoulder: ({left_shoulder.x:.2f}, {left_shoulder.y:.2f})", (10, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        y_offset += 20

        # Print right shoulder coordinates
        cv2.putText(image, f"Right Shoulder: ({right_shoulder.x:.2f}, {right_shoulder.y:.2f})", (10, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        y_offset += 20

        # Print waist coordinates
        cv2.putText(image, f"Waist: ({waist.x:.2f}, {waist.y:.2f})", (10, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 0, 0), 1)
        y_offset += 20

        # Print chest coordinates
        cv2.putText(image, f"Chest: ({chest.x:.2f}, {chest.y:.2f})", (10, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 0, 0), 1)
        y_offset += 20

        # Print left elbow coordinates
        cv2.putText(image, f"Left Elbow: ({left_elbow.x:.2f}, {left_elbow.y:.2f})", (10, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        y_offset += 20

        # Print right elbow coordinates
        cv2.putText(image, f"Right Elbow: ({right_elbow.x:.2f}, {right_elbow.y:.2f})", (10, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        y_offset += 20

        # Print left wrist coordinates
        cv2.putText(image, f"Left Wrist: ({left_wrist.x:.2f}, {left_wrist.y:.2f})", (10, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        y_offset += 20

        # Print right wrist coordinates
        cv2.putText(image, f"Right Wrist: ({right_wrist.x:.2f}, {right_wrist.y:.2f})", (10, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        y_offset += 20

        # Print middle finger coordinates
        cv2.putText(image, f"Middle Finger: ({middle_finger.x:.2f}, {middle_finger.y:.2f})", (10, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        y_offset += 20

        # Print left knee coordinates
        cv2.putText(image, f"Left Knee: ({left_knee.x:.2f}, {left_knee.y:.2f})", (10, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        y_offset += 20





        #calculated various distances
        shoulder_dist = np.sqrt((left_shoulder.x - right_shoulder.x) ** 2 + (left_shoulder.y - right_shoulder.y) ** 2)
        waist_chest_dist = np.sqrt((waist.x - chest.x) ** 2 + (waist.y - chest.y) ** 2)
        elbow_dist = np.sqrt((left_elbow.x - right_elbow.x) ** 2 + (left_elbow.y - right_elbow.y) ** 2)
        shoulder_elbow_dist = np.sqrt((left_shoulder.x - left_elbow.x) ** 2 + (left_shoulder.y - left_elbow.y) ** 2)
        knee_dist = np.sqrt((left_knee.x - right_knee.x) ** 2 + (left_knee.y - right_knee.y) ** 2)
        middle_finger_dist = np.sqrt((left_middle_finger_tip.x - right_middle_finger_tip.x) ** 2 + (left_middle_finger_tip.y - right_middle_finger_tip.y) ** 2)

        #gesture detection
        # Determine the pose
        # if shoulder_dist > 0.5 and waist_chest_dist > 0.5 and elbow_dist > 0.5 and shoulder_elbow_dist > 0.3 and middle_finger_dist < 0.3:
        #     cv2.putText(image, "Right Hand Up", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        #     # Press the 'w' key
        #     # key = cv2.waitKey(1) & 0xFF
        #     # if key == ord('w'):
        #     #     print("Pressed 'w' key")
        # if shoulder_dist > 0.5 and waist_chest_dist > 0.5 and elbow_dist > 0.5 and shoulder_elbow_dist < 0.3 and middle_finger_dist < 0.3:
        #     cv2.putText(image, "Left Hand Up", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        #     # Press the 's' key
        #     # key = cv2.waitKey(1) & 0xFF
        #     # if key == ord('s'):
        #     #     print("Pressed 's' key")
        # if left_shoulder.x < right_shoulder.x and left_knee.y < right_knee.y and left_middle_finger_tip.x > right_middle_finger_tip.x :
        #     cv2.putText(image, "Arms Crossed", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        #     # Press the 'd' key
        #     # key = cv2.waitKey(1) & 0xFF
        #     # if key == ord('d'):
        #     #     print("Pressed 'd' key")
        # if left_shoulder.x < right_shoulder.x and left_knee.y > right_knee.y:
        #     cv2.putText(image, "Sitting Position", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        #     # Press the 'a' key
        #     # key = cv2.waitKey(1) & 0xFF
        #     # if key == ord('a'):
        #     #     print("Pressed 'a' key")
        # if shoulder_dist > 0.5 and waist_chest_dist > 0.5 and elbow_dist > 0.5 and shoulder_elbow_dist < 0.3 and middle_finger_dist > 0.3:
        #     cv2.putText(image, "Both Hands Up", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        #     # Press the 'x' key
        #     # key = cv2.waitKey(1) & 0xFF
        #     # if key == ord('x'):
        #     #     print("Pressed 'x' key")
        # else:
        #     cv2.putText(image, "No Gesture Detected", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)



        # if right_elbow.y > right_wrist.y and right_shoulder.y < right_wrist.y and right_wrist.x < 0.5:
        #     cv2.putText(image, "Move Right", (10, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        def hold_Z(hold_time):
            import time
            start = time.time()
            while time.time() - start < hold_time:
                pyautogui.press('Z')

        def hold_X(hold_time):
            import time
            start = time.time()
            while time.time() - start < hold_time:
                pyautogui.press('x')

        if right_shoulder.y < right_wrist.y < right_elbow.y:
            cv2.putText(image, "Move Right", (10, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            pyautogui.press('w')

        elif left_shoulder.y < left_wrist.y < left_elbow.y:
            cv2.putText(image, "Move Left", (10, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            pyautogui.press('s')

        elif right_shoulder.y > right_elbow.y:
            cv2.putText(image, "Right Hand up", (10, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            pyautogui.press('z')

        elif left_shoulder.y > left_elbow.y:
            cv2.putText(image, "Left Hand up", (10, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            hold_Z(3)

        elif left_shoulder.y > left_wrist.y and left_shoulder.y < left_elbow.y and right_shoulder.y > right_wrist.y and right_shoulder.y < right_elbow.y:
            cv2.putText(image, "Defence", (10, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            pyautogui.press('x')


        elif right_elbow.y < right_wrist.y and right_shoulder.y < right_elbow.y and left_elbow.y< left_wrist.y and left_shoulder.y < left_elbow.y :
            cv2.putText(image, "Standing", (10, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)



    cv2.imshow('Detection Model', image)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

