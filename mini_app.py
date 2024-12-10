import tkinter as tk
from tkinter import messagebox
import create_student_csv

def run_mini_app():
    def capture_images():
        try:
            create_student_csv.capture_images()
            messagebox.showinfo("Success", "Images captured successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to capture images: {e}")

    root = tk.Tk()
    root.title("Capture Student Images")
    root.geometry("300x150")

    tk.Label(root, text="Image Capture Tool", font=("Arial", 16)).pack(pady=10)
    tk.Button(root, text="Capture Images", command=capture_images, width=20).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_mini_app()
