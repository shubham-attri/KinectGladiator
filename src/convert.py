import tensorflow as tf
json_file_path = "venv/my-pose-model/model.json"
with open(json_file_path, "r") as json_file:
    json_savedModel= json_file.read()
model_json = tf.keras.models.model_from_json(json_savedModel)
model_json.save("model_name.h5", save_format="hf")