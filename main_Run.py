import tkinter as tk
from tkinter import messagebox
import create_student_csv
import training
import testing
import os

def main_app():
    root = tk.Tk()
    root.title("Attendance Management System")
    root.geometry("400x300")

    def capture_images():
        os.system("python create_student_csv.py")

    def train_images():
        training.train_model()

    def recognize_faces():
        testing.recognize_faces()

    tk.Button(root, text="Take Images", command=capture_images, width=20).pack(pady=10)
    tk.Button(root, text="Train Images", command=train_images, width=20).pack(pady=10)
    tk.Button(root, text="Automatic Attendance", command=recognize_faces, width=20).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_app()