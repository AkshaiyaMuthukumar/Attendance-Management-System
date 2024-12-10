import streamlit as st
import pandas as pd
import os

def load_data():
    attendance_dir = "Attendance"
    if not os.path.exists(attendance_dir):
        os.makedirs(attendance_dir)
    all_files = [f for f in os.listdir(attendance_dir) if f.endswith(".csv")]
    return all_files

def display_attendance(file_name):
    file_path = os.path.join("Attendance", file_name)
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        st.dataframe(df)
    else:
        st.error("File not found!")

def main():
    st.title("Attendance Management System")
    st.sidebar.header("Navigation")
    option = st.sidebar.selectbox("Choose an option:", ["Home", "View Attendance"])

    if option == "Home":
        st.write("Welcome to the Attendance Management System.")
        st.write("Navigate to **View Attendance** to see attendance records.")
    elif option == "View Attendance":
        st.write("### View Attendance Records")
        attendance_files = load_data()
        if attendance_files:
            file_name = st.selectbox("Select a file:", attendance_files)
            display_attendance(file_name)
        else:
            st.warning("No attendance records found.")

if __name__ == "__main__":
    main()
