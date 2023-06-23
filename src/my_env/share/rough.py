import cv2
import mediapipe as mp
import numpy as np
import pyautogui as pyautogui

# Initialize Mediapipe Pose.
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Initialize Video Stream.
cap = cv2.VideoCapture(0)

# Loop through video frames.
while cap.isOpened():
    ret, image = cap.read()
    if not ret:
        print("Ignoring empty camera frame.")
        continue

    # Convert the BGR image to RGB.
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Use Mediapipe Pose to get landmarks.
    results = pose.process(image)

    # Check if landmarks are detected.
    if results.pose_landmarks is not None:
        # Get landmarks of interest.
        landmarks = results.pose_landmarks.landmark
        left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
        right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
        waist = landmarks[24]
        chest = landmarks[12]
        left_elbow = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value]
        right_elbow = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value]
        left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]
        right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]
        middle_finger = landmarks[20]

        # Calculate distances between landmarks.
        shoulder_dist = np.sqrt((right_shoulder.x - left_shoulder.x) ** 2 + (right_shoulder.y - left_shoulder.y) ** 2)
        waist_chest_dist = np.sqrt((waist.x - chest.x) ** 2 + (waist.y - chest.y) ** 2)
        elbow_dist = np.sqrt((right_elbow.x - left_elbow.x) ** 2 + (right_elbow.y - left_elbow.y) ** 2)
        shoulder_elbow_dist = np.sqrt((right_elbow.x - right_shoulder.x) ** 2 + (right_elbow.y - right_shoulder.y) ** 2)
        middle_finger_dist = np.sqrt((middle_finger.x - right_wrist.x) ** 2 + (middle_finger.y - right_wrist.y) ** 2)

        # Determine the pose.
        # Determine the pose
        if shoulder_dist > 0.5 and waist_chest_dist > 0.5 and elbow_dist > 0.5 and shoulder_elbow_dist > 0.3 and middle_finger_dist < 0.3:
            cv2.putText(image, "Right Hand Up", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            pyautogui.press('d')
            # Press the 'w' key
            # key = cv2.waitKey(1) & 0xFF
            # if key == ord('w'):
            #     print("Pressed 'w' key")
        elif shoulder_dist > 0.5 and waist_chest_dist > 0.5 and elbow_dist > 0.5 and shoulder_elbow_dist < 0.3 and middle_finger_dist < 0.3:
            cv2.putText(image, "Left Hand Up", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            pyautogui.press('a')
            # Press the 's' key
            # key = cv2.waitKey(1) & 0xFF
            # if key == ord('s'):
            #     print("Pressed 's' key")
        elif shoulder_dist < 0.3 and waist_chest_dist < 0.3 and elbow_dist < 0.3:
            cv2.putText(image, "Arm Crossed", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            pyautogui.press('x')
            # Press the 'a' key
            # key = cv2.waitKey(1) & 0xFF
            # if key == ord('a'):
            #     print("Pressed 'a' key")
        elif shoulder_dist > 0.5 and waist_chest_dist > 0.5 and elbow_dist > 0.5 and shoulder_elbow_dist < 0.3 and middle_finger_dist > 0.5:
            cv2.putText(image, "Right Hand Down", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            pyautogui.press('c')
            # Press the 'd' key
            # key = cv2.waitKey(1) & 0xFF
            # if key == ord('d'):
            #     print("Pressed 'd' key")

        cv2.imshow("Hand Tracking", image)

        # Quit the program when 'q' is pressed
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break


# Release the capture
cap.release()
cv2.destroyAllWindows()

# import cv2
# import mediapipe as mp
# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
# mp_pose = mp.solutions.pose
#
# # For static images:
# IMAGE_FILES = []
# BG_COLOR = (192, 192, 192) # gray
# with mp_pose.Pose(
#     static_image_mode=True,
#     model_complexity=2,
#     enable_segmentation=True,
#     min_detection_confidence=0.5) as pose:
#   for idx, file in enumerate(IMAGE_FILES):
#     image = cv2.imread(file)
#     image_height, image_width, _ = image.shape
#     # Convert the BGR image to RGB before processing.
#     results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#
#     if not results.pose_landmarks:
#       continue
#     print(
#         f'Nose coordinates: ('
#         f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width}, '
#         f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_height})'
#     )

#     annotated_image = image.copy()
#     # Draw segmentation on the image.
#     # To improve segmentation around boundaries, consider applying a joint
#     # bilateral filter to "results.segmentation_mask" with "image".
#     condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
#     bg_image = np.zeros(image.shape, dtype=np.uint8)
#     bg_image[:] = BG_COLOR
#     annotated_image = np.where(condition, annotated_image, bg_image)
#     # Draw pose landmarks on the image.
#     mp_drawing.draw_landmarks(
#         annotated_image,
#         results.pose_landmarks,
#         mp_pose.POSE_CONNECTIONS,
#         landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
#     cv2.imwrite('/tmp/annotated_image' + str(idx) + '.png', annotated_image)
#     # Plot pose world landmarks.
#     mp_drawing.plot_landmarks(
#         results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)
#
# # For webcam input:
# cap = cv2.VideoCapture(0)
# with mp_pose.Pose(
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5) as pose:
#   while cap.isOpened():
#     success, image = cap.read()
#     if not success:
#       print("Ignoring empty camera frame.")
#       # If loading a video, use 'break' instead of 'continue'.
#       continue
#
#     # To improve performance, optionally mark the image as not writeable to
#     # pass by reference.
#     image.flags.writeable = False
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     results = pose.process(image)
#
#     # Draw the pose annotation on the image.
#     image.flags.writeable = True
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#     mp_drawing.draw_landmarks(
#         image,
#         results.pose_landmarks,
#         mp_pose.POSE_CONNECTIONS,
#         landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
#     # Flip the image horizontally for a selfie-view display.
#     cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
#     if cv2.waitKey(5) & 0xFF == 27:
#       break
# cap.release()