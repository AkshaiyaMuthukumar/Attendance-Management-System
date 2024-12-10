import os
import cv2
import pandas as pd

def capture_images():
    if not os.path.exists("StudentDetails"):
        os.makedirs("StudentDetails")

    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")

    student_details_path = "StudentDetails/student_details.csv"
    if not os.path.exists(student_details_path):
        df = pd.DataFrame(columns=["StudentID", "StudentName"])
        df.to_csv(student_details_path, index=False)

    df = pd.read_csv(student_details_path)
    df = pd.concat([df, pd.DataFrame([[student_id, student_name]], columns=["StudentID", "StudentName"])], ignore_index=True)
    df.to_csv(student_details_path, index=False)

    cam = cv2.VideoCapture(0)
    count = 0
    if not os.path.exists("TrainingImage"):
        os.makedirs("TrainingImage")

    while True:
        ret, frame = cam.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cv2.CascadeClassifier("haarcascade_frontalface_default.xml").detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            count += 1
            cv2.imwrite(f"TrainingImage/{student_id}_{count}.jpg", gray[y:y + h, x:x + w])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow("Image Capture", frame)
        if cv2.waitKey(1) & 0xFF == ord("q") or count >= 20:
            break
    cam.release()
    cv2.destroyAllWindows()
    print(f"Images captured successfully for {student_name} (ID: {student_id})!")

if __name__ == "__main__":
    capture_images()
