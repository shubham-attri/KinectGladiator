import mediapipe as mp
import keyboard
import cv2
import pyautogui


screenWidth, screenHeight = pyautogui.size()
print("Screen width:", screenWidth)


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose




cap = cv2.VideoCapture(0)


while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue


    # Convert the image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


    # Detect the pose
    with mp_pose.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as pose:
        results = pose.process(image)
       
        # Print the coordinates of each detected landmark
        if results.pose_landmarks is not None:
            # print(type(results.pose_landmarks))
            for idx, landmark in enumerate(results.pose_landmarks.landmark):
                if idx == 15:
                    print("Landmark {}: ({}, {})".format(idx, landmark.x, landmark.y))
                    #keyboard.press_and_release("R")
                if idx == 16:
                    print("Landmark {}: ({}, {})".format(idx, landmark.x, landmark.y))


    # Draw the pose landmarks on the image
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)


    # Display the image
    cv2.imshow('MediaPipe Pose', image)


    # Quit the program when 'q' is pressed
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break


# Release the capture
cap.release()
cv2.destroyAllWindows()
