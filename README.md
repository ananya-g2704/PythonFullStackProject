# Attendance Tracker

## Description:
The Attendance Tracker is a Python-based system to record and manage attendance. It starts as a simple Tkinter app with CSV storage and can be extended with email reminders, face recognition using OpenCV, and a web-based version using Django for database management and report generation.

## Features:
Automated Attendance Logging – Mark attendance using face recognition (or manually).
User Management – Add, edit, and delete student/employee records.
Date & Time Stamping – Record exact check-in/check-out times automatically.
Data Storage & Reports – Store attendance in CSV, Excel, or database; generate daily/weekly/monthly reports.
Analytics & Visualization – Show attendance trends and statistics through graphs and dashboards.
Security & Access Control – Optional admin login to prevent unauthorized access.
 
 ## Project Structure:

 ATTENDANCE TRACKER/
|
|---src/   # core application logic 
|    |---logic.py   # Business logic and task 
operations
|   |__db.py   # Database operations
|
|---API/         # Backend API
|   |__main.py   # FastAPI endpoints
|
|---|frontend/     # Frontend applications
|     |__app.py      # Streamlit web interface
|
|___requirements.txt   # Python Dependencies
|
|___README.md          # Project documentation
|
|
|___.env       # Python Variables 

## Quick Start

### Prerequisites

-Python 3.8 or higher
-A Supabase Account
-Git(Push,cloning)
 
### 1.Clone or download the project
 # Option 1: Clone with Git
 git clone <repository url>

 # Option 2:Download and extract the ZIP file

### 2.Install Dependencies
  
  # install all required python packages
  pip install -r  requirements.txt

###  3.Setup supabase database

1.Create a supabase project
2.Create the task tables:
   -Go to the sql editor in your supabase  dashboard
   -Run this sql command:
   ```sql
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    registration_date DATE,
    photo_path VARCHAR(255),
    face_encoding TEXT
);
CREATE TABLE attendance (
    attendance_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(student_id),
    attendance_date DATE NOT NULL,
    attendance_time TIME,
    attendance_status VARCHAR(10) CHECK (attendance_status IN ('Present', 'Absent', 'Late')),
    class_or_subject VARCHAR(50),
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
3. **Get Your Credentials:

### 4.Configure environment Variable

1.Create a `.env` file in the project root

2.Add your Supabase credentials to `.env`;
SUPABASE_URL=your_project_url_here
SUPABASE_KEY=your_anon_key_here

**Example:**
SUPABASE_URL="https://lbnpwbadakbkxsrxinhw.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxibnB3YmFkYWtia3hzcnhpbmh3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODEzMDksImV4cCI6MjA3MzY1NzMwOX0.Ubf2RSw-F5epSCecD7nooLFgT6u3pDgjdbja6u5sZw0"

### 5. Run the Application

## Streamlit Frontend
streamlit run frontend/app.py

The app will open in your browser at `http://localhost:8080`

## FastAPI Backend

cd API
python main.py
 
The API will be available at `http://localhost:8081`

## How to use

**Frontend**:Streamlit(Python web framework)
**Backend**:FastAPI(Python REST API framework)
**Database**:Supabase(PostgreSQL-based backend-as-a-service)
**Language**:Python 3.8+

### Key Components

1.**`src/db.py`** :Database operations
   - Handles all CRUD operations with Supabase
2.**`src/logic.py`**:Business logic
    - Task validation and processing


## Troubleshooting

## Common Issues

1.**"Module not found" Errors**
     - Make sure you've installed all dependencies: `pip install -r requirements.txt`
     - Check that you've running commands from the correct directory
    
## Future Enhancements

Ideas for extending this project:

- **USer Authentication**:Add user accounts and login
- **Task Categories**:Organize tasks by subject or category
- **Notifications**:Email or push notifications for due dates
- **File Attachments**:Attach files to tasks
- **Collaboration**:Share tasks with classmates
- **Mobile App**:React Native or Flutter mobile version
- **Data Export**:Export tasks to CSV or PDF
-  **TAsk Templates**:Create reusable task templates

## Support

If you encounter any issues or have questions:
Phone number:`9014277375`
Email:`ananya.g2704@gmail.com`