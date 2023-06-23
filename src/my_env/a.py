import mediapipe as mp
import keyboard
import cv2
import pyautogui


screenWidth, screenHeight = pyautogui.size()
print("Screen width:", screenWidth)

#
# mp_drawing = mp.solutions.drawing_utils
# mp_pose = mp.solutions.pose
#
#
#
#
# cap = cv2.VideoCapture(0)
#
#
# while cap.isOpened():
#     success, image = cap.read()
#     if not success:
#         print("Ignoring empty camera frame.")
#         continue
#
#
#     # Convert the image to RGB
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#
#
#     # Detect the pose
#     with mp_pose.Pose(
#             min_detection_confidence=0.5,
#             min_tracking_confidence=0.5) as pose:
#         results = pose.process(image)
#
#         # Print the coordinates of each detected landmark
#         if results.pose_landmarks is not None:
#             # print(type(results.pose_landmarks))
#             for idx, landmark in enumerate(results.pose_landmarks.landmark):
#                 if idx == 15:
#                     print("Landmark {}: ({}, {})".format(idx, landmark.x, landmark.y))
#                     # keyboard.press_and_release("R")
#                     pyautogui.press('a')
#
#                 if idx == 16:
#                     print("Landmark {}: ({}, {})".format(idx, landmark.x, landmark.y))
#
#
#     # Draw the pose landmarks on the image
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#     mp_drawing.draw_landmarks(
#         image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
#
#
#     # Display the image
#     cv2.imshow('MediaPipe Pose', image)
#
#
#     # Quit the program when 'q' is pressed
#     if cv2.waitKey(5) & 0xFF == ord('q'):
#         break
#
#
# # Release the capture
# cap.release()
# cv2.destroyAllWindows()
#


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Flip the image horizontally for a later selfie-view display
        image = cv2.flip(image, 1)

        # Convert the image to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # To improve performance, optionally mark the image as not writeable to pass by reference.
        image.flags.writeable = False
        results = hands.process(image)

        # Draw the landmarks and connections on the image
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=hand_landmarks,
                    connections=mp_hands.HAND_CONNECTIONS,
                    landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=2),
                    connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2))
                # Get the coordinates of the landmarks of the hand
                landmarks = [[landmark.x, landmark.y, landmark.z] for landmark in hand_landmarks.landmark]

                # Get the x-coordinate of the middle finger tip
                middle_finger_tip_x = landmarks[12][0]

                # Get the x-coordinate of the wrist
                wrist_x = landmarks[0][0]

                # Calculate the distance between the middle finger tip and the wrist
                distance = middle_finger_tip_x - wrist_x

                # Determine whether the hand is left or right based on the direction of the distance
                if distance > 0:
                    hand = "right"
                else:
                    hand = "left"

                # Determine whether the hand is up based on the y-coordinate of the middle finger tip
                middle_finger_tip_y = landmarks[12][1]
                if middle_finger_tip_y < landmarks[0][1]:
                    position = "up"
                else:
                    position = "down"

                # Print the result
                print(f"{hand} hand is {position}")

        # Display the image
        cv2.imshow("Hand Tracking", image)

        # Quit the program when 'q' is pressed
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

# Release the capture
cap.release()
cv2.destroyAllWindows()