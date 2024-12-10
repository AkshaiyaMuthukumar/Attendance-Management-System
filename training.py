import cv2
import numpy as np
import os
from PIL import Image

def train_model():
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Path to the folder where training images are stored
    path = 'TrainingImage'

    # Lists to hold faces and their corresponding labels
    faces = []
    labels = []

    # Read all the image files from the folder and prepare them for training
    for image_name in os.listdir(path):
        if image_name.endswith(".jpg") or image_name.endswith(".png"):
            image_path = os.path.join(path, image_name)
            image = Image.open(image_path).convert('L')  # Convert to grayscale
            image_array = np.array(image, 'uint8')

            # Extract student ID from the image filename (e.g., 'S001_1.jpg' -> 'S001')
            student_id = int(image_name.split('_')[0][1:])  # Extract ID part (S001)

            faces.append(image_array)
            labels.append(student_id)

    # Train the model
    recognizer.train(faces, np.array(labels))

    # Save the trained model to 'TrainingImageLabel/training.yml'
    recognizer.save('TrainingImageLabel/training.yml')

    print("Model trained and saved successfully!")

if __name__ == '__main__':
    train_model()
