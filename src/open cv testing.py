import cv2
import numpy as np
import tensorflow as tf


# Load the Teachable Machine model from a JSON file
model_url = "https://teachablemachine.withgoogle.com/models/M0K8XxFi8/"
model = tf.keras.models.model_from_json(tf.keras.utils.get_file('model.json', model_url + 'model.json'))

# Load the model weights
weights_url = model_url + "weights.bin"
model.load_weights(tf.keras.utils.get_file('weights.bin', weights_url, cache_subdir='models'))

# Define the classes
classes = ['Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5', 'Class 6']

# Set up the video capture
cap = cv2.VideoCapture(0)

# Process the video frames
while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Preprocess the frame
    resized_frame = cv2.resize(frame, (224, 224))
    resized_frame = np.expand_dims(resized_frame, axis=0)

    # Normalize the frame
    normalized_frame = resized_frame / 255.0

    # Predict the class of the frame
    predictions = model.predict(normalized_frame)
    class_index = np.argmax(predictions)

    # Display the class label on the frame
    class_label = classes[class_index]
    cv2.putText(frame, class_label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Show the frame
    cv2.imshow('Teachable Machine Model', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()
