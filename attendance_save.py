import pandas as pd
import os
from datetime import datetime

def save_attendance(student_id, student_name):
    # Ensure Attendance folder exists
    attendance_folder = "Attendance"
    if not os.path.exists(attendance_folder):
        os.makedirs(attendance_folder)

    # Define file path
    file_path = os.path.join(attendance_folder, "attendance.csv")

    # Check if the file exists (create header if not)
    if not os.path.isfile(file_path):
        df = pd.DataFrame(columns=["StudentID", "StudentName", "Date", "Time"])
        df.to_csv(file_path, index=False)

    # Add attendance data
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")
    data = pd.DataFrame([[student_id, student_name, current_date, current_time]], columns=["StudentID", "StudentName", "Date", "Time"])

    # Append new record to the file
    data.to_csv(file_path, mode='a', header=False, index=False)

    print(f"Attendance for {student_name} (ID: {student_id}) added successfully!")
