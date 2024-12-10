import cv2
import pandas as pd
import numpy as np
import os

def recognize_faces():
    # Load the trained model
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    try:
        recognizer.read("TrainingImageLabel/training.yml")  # Ensure this file exists
    except cv2.error as e:
        print(f"Error reading the trained model: {e}")
        return

    # Load student details from the 'StudentDetails' folder (update the path accordingly)
    try:
        df = pd.read_csv("StudentDetails/student_details.csv")  # Path to CSV file
    except FileNotFoundError as e:
        print(f"Error reading student details: {e}")
        return

    # Load the Haar Cascade for face detection (ensure the XML file is in the correct path)
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            
            # Recognize the face
            id_, conf = recognizer.predict(roi_gray)
            if conf >= 45 and conf <= 85:
                # Retrieve student details from CSV
                student_data = df.loc[df["StudentID"] == id_]
                if not student_data.empty:
                    student_name = student_data.iloc[0]["StudentName"]
                    print(f"Recognized: {student_name}")
                    
                    # Draw rectangle and label on face
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    cv2.putText(frame, student_name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

            else:
                cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        # Display the frame with the face recognition
        cv2.imshow("Face Recognition", frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Run the function when the script is executed
if __name__ == "__main__":
    recognize_faces()
