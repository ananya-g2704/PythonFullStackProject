# db_manager.py
import os
from supabase import create_client
from dotenv import load_dotenv

# Load environment variables 
load_dotenv()
url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")

supabase =create_client(url,key)


# ----------
# Student Table operations
# ----------

# Create Student
def create_student(student_name, registration_date, photo_path=None, face_encoding=None):
    return supabase.table("students").insert({
        "student_name": student_name,
        "registration_date": registration_date,
        "photo_path": photo_path,
        "face_encoding": face_encoding
    }).execute()


# Get All Students
def get_all_students():
    return supabase.table("students").select("*").order("registration_date").execute()

# Update Student Info
def update_student(student_id, updates: dict):
    return supabase.table("students").update(updates).eq("student_id", student_id).execute()

# Delete Student
def delete_student(student_id):
    return supabase.table("students").delete().eq("student_id", student_id).execute()




# ----------
# Attendance Table oprations
# ----------

# Create Attendance
def create_student(student_name, registration_date, photo_path=None, face_encoding=None):
    return supabase.table("students").insert({
        "student_name": student_name,
        "registration_date": registration_date,
        "photo_path": photo_path,
        "face_encoding": face_encoding
    }).execute()

# Get All Attendance Records
def get_all_attendance():
    return supabase.table("attendance").select("*").order("attendance_date").execute()

# Update Attendance 
def update_attendance(attendance_id, updates: dict):
    return supabase.table("attendance").update(updates).eq("attendance_id",attendance_id).execute()   

# Delete Attendance Record
def delete_attendance(attendance_id):
    return supabase.table("attendance").delete().eq("attendance_id",attendance_id).execute()