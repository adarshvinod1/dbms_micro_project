import customtkinter as ctk
from tkinter import messagebox
import mysql.connector as mc

def DB_Connect(code, op):
    global resultArr
    resultArr = []
    m1 = mc.connect(host="localhost", user="root", passwd="7561", database="microdb")
    c1 = m1.cursor()

    try:
        c1.execute(code)
    except Exception as e:
        messagebox.showerror("Database Error", f"Error in executing the query: {str(e)}")
    
    if op == 1:
        resultArr = c1.fetchall()

    m1.commit()
    c1.close()
    m1.close()

def login_access(uname, passwd):
    DB_Connect(f"SELECT password FROM login WHERE user_id = '{uname}'", 1)
    try:
        if resultArr and resultArr[0][0] == passwd:
            messagebox.showinfo("Login", "Granted!")
            return uname  # Return username for further checks
        else:
            messagebox.showerror("Login", "Invalid Username or Password!")
            return None
    except Exception:
        messagebox.showerror("Login", "Invalid Username or Password!")
        return None

def show_student_details(student_id):
    student_window = ctk.CTkToplevel(root)
    student_window.title("Student Details")
    student_window.geometry("600x400")
    title = ctk.CTkLabel(student_window, text="STUDENT DETAILS", font=("Arial", 30))
    title.pack(pady=20)

    # Fetch student details
    DB_Connect(f"SELECT s_name, s_dob, s_phone, s_mail, dept_id FROM student WHERE s_id = '{student_id}'", 1)
    
    if resultArr:
        student_data = resultArr[0]
        dept_id = student_data[4]

        # Create a frame for the details
        details_frame = ctk.CTkFrame(student_window)
        details_frame.pack(pady=20)

        # Create the column headings
        headings = ["Name", "DOB", "Phone", "Email", "Department"]
        for idx, heading in enumerate(headings):
            label = ctk.CTkLabel(details_frame, text=heading, font=("Arial", 14))
            label.grid(row=0, column=idx, padx=10, pady=10)

        # Populate the student data
        student_info = list(student_data[:-1]) + [dept_id]  # Exclude dept_id
        for idx, info in enumerate(student_info):
            label = ctk.CTkLabel(details_frame, text=info, font=("Arial", 14))
            label.grid(row=1, column=idx, padx=10, pady=5)

        # Fetch marks with subject names
        DB_Connect(f"""
            SELECT sub.sub_name, m.mark 
            FROM mark m 
            JOIN subject sub ON m.sub_id = sub.sub_id 
            WHERE m.s_id = '{student_id}'
        """, 1)
        marks_data = resultArr

        # Fetch attendance with subject names
        DB_Connect(f"""
            SELECT sub.sub_name, a.attendance 
            FROM attendance a 
            JOIN subject sub ON a.sub_id = sub.sub_id 
            WHERE a.s_id = '{student_id}'
        """, 1)
        attendance_data = resultArr
        
        # Create a frame for marks and attendance
        marks_frame = ctk.CTkFrame(student_window)
        marks_frame.pack(pady=20)

        marks_heading = ctk.CTkLabel(marks_frame, text="Marks", font=("Arial", 16))
        marks_heading.pack(pady=10)

        # Display marks
        for sub_name, marks in marks_data:
            label = ctk.CTkLabel(marks_frame, text=f"{sub_name}: Marks = {marks}", font=("Arial", 14))
            label.pack(pady=5)
        
        # Display attendance
        attendance_heading = ctk.CTkLabel(marks_frame, text="Attendance", font=("Arial", 16))
        attendance_heading.pack(pady=10)

        for sub_name, attendance in attendance_data:
            label = ctk.CTkLabel(marks_frame, text=f"{sub_name}: Attendance = {attendance}", font=("Arial", 14))
            label.pack(pady=5)

def show_faculty_details(faculty_id):
    faculty_window = ctk.CTkToplevel(root)
    faculty_window.title("Faculty Details")
    faculty_window.geometry("600x400")

    title = ctk.CTkLabel(faculty_window, text="FACULTY DETAILS", font=("Arial", 30))
    title.pack(pady=20)

    # Fetch faculty details
    DB_Connect(f"SELECT f_name, f_phone, f_mail, dept_id FROM faculty WHERE f_id = '{faculty_id}'", 1)

    if resultArr:
        faculty_data = resultArr[0]
        dept_id = faculty_data[3]
        
        # Map department IDs to names
        dept_names = {
            "cs": "Computer Science",
            "ec": "Electronics",
            "ce": "Civil",
            "me": "Mechanical",
            "ei": "Instrumentation"
        }
        
        dept_name = dept_names.get(dept_id, "Unknown Department")

        # Create a frame for the details
        details_frame = ctk.CTkFrame(faculty_window)
        details_frame.pack(pady=20)

        # Create the column headings
        headings = ["Name", "Phone", "Email", "Department"]
        for idx, heading in enumerate(headings):
            label = ctk.CTkLabel(details_frame, text=heading, font=("Arial", 14))
            label.grid(row=0, column=idx, padx=10, pady=10)

        # Populate the faculty data
        faculty_info = list(faculty_data[:3]) + [dept_name]
        for idx, info in enumerate(faculty_info):
            label = ctk.CTkLabel(details_frame, text=info, font=("Arial", 14))
            label.grid(row=1, column=idx, padx=10, pady=5)

def login():
    username = username_entry.get()
    password = password_entry.get()
    user_role = login_access(username, password)
    
    if user_role:
        if username[0] == 's':
            show_student_details(username)
        elif username[0] == 'f':
            show_faculty_details(username)

def show_insertion_forms():
    if username_entry.get()[0] == 'a':  # Check if the user is an admin
        insertion_window = ctk.CTkToplevel(root)
        insertion_window.title("Insert Data")
        insertion_window.geometry("600x600")  # Adjusted height for more fields

        # Create a title for insertion forms
        title = ctk.CTkLabel(insertion_window, text="INSERT DATA", font=("Arial", 24))
        title.pack(pady=20)

        # Create a scrollable frame for insertion forms
        scrollable_frame = ctk.CTkScrollableFrame(insertion_window)
        scrollable_frame.pack(fill='both', expand=True)

        # Create buttons for different actions
        ctk.CTkLabel(scrollable_frame, text="Choose an Action:", font=("Arial", 18)).pack(pady=20)

        # Button for Student Data Insertion
        insert_student_button = ctk.CTkButton(scrollable_frame, text="Insert Student Data",
                                                command=lambda: show_student_insertion(scrollable_frame))
        insert_student_button.pack(pady=10)

        # Button for Faculty Data Insertion
        insert_faculty_button = ctk.CTkButton(scrollable_frame, text="Insert Faculty Data",
                                                command=lambda: show_faculty_insertion(scrollable_frame))
        insert_faculty_button.pack(pady=10)

        # Button for Marks Update
        update_marks_button = ctk.CTkButton(scrollable_frame, text="Update Student Marks",
                                              command=lambda: show_marks_update(scrollable_frame))
        update_marks_button.pack(pady=10)

    else:
        messagebox.showwarning("Access Denied", "Only admins can access insertion forms.")

def show_insertion_forms():
    if username_entry.get()[0] == 'a':  # Check if the user is an admin
        insertion_window = ctk.CTkToplevel(root)
        insertion_window.title("Insert Data")
        insertion_window.geometry("600x600")  # Adjusted height for more fields

        # Create a title for insertion forms
        title = ctk.CTkLabel(insertion_window, text="INSERT DATA", font=("Arial", 24))
        title.pack(pady=20)

        # Create a scrollable frame for insertion forms
        scrollable_frame = ctk.CTkScrollableFrame(insertion_window)
        scrollable_frame.pack(fill='both', expand=True)

        # Create buttons for different actions
        ctk.CTkLabel(scrollable_frame, text="Choose an Action:", font=("Arial", 18)).pack(pady=20)

        # Button for Student Data Insertion
        insert_student_button = ctk.CTkButton(scrollable_frame, text="Insert Student Data",
                                                command=lambda: show_student_insertion(scrollable_frame))
        insert_student_button.pack(pady=10)

        # Button for Faculty Data Insertion
        insert_faculty_button = ctk.CTkButton(scrollable_frame, text="Insert Faculty Data",
                                                command=lambda: show_faculty_insertion(scrollable_frame))
        insert_faculty_button.pack(pady=10)

        # Button for Marks Update
        update_marks_button = ctk.CTkButton(scrollable_frame, text="Update Student Marks",
                                              command=lambda: show_marks_update(scrollable_frame))
        update_marks_button.pack(pady=10)

        # Button for Attendance Update
        update_attendance_button = ctk.CTkButton(scrollable_frame, text="Update Student Attendance",
                                                  command=lambda: show_attendance_update(scrollable_frame))
        update_attendance_button.pack(pady=10)

         # Button for Student mark Insertion
        insert_marks_button = ctk.CTkButton(scrollable_frame, text="Insert Student mark",
                                                command=lambda: mark_insertion(scrollable_frame))          
        insert_marks_button.pack(pady=10)

        # Button for Student attendace Insertion
        insert_attendance_button = ctk.CTkButton(scrollable_frame, text="Insert Student attendance",
                                                command=lambda: attendace_insertion(scrollable_frame))          
        insert_attendance_button.pack(pady=10)
    else:
        messagebox.showwarning("Access Denied", "Only admins can access insertion forms.")

def attendace_insertion(scrollable_frame):
    global a_attendance_student_id_entry,a_attendance_subject_id_entry,a_new_attendance_entry;
    # Clear previous entries
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    ctk.CTkLabel(scrollable_frame, text="Insert Student Attendance", font=("Arial", 20)).pack(pady=20)
    ctk.CTkLabel(scrollable_frame, text="Student ID:").pack(pady=5)
    a_attendance_student_id_entry = ctk.CTkEntry(scrollable_frame)
    a_attendance_student_id_entry.pack(pady=5)

    ctk.CTkLabel(scrollable_frame, text="Subject ID:").pack(pady=5)
    a_attendance_subject_id_entry = ctk.CTkEntry(scrollable_frame)
    a_attendance_subject_id_entry.pack(pady=5)

    ctk.CTkLabel(scrollable_frame, text="New Attendance:").pack(pady=5)
    a_new_attendance_entry = ctk.CTkEntry(scrollable_frame)
    a_new_attendance_entry.pack(pady=5)

    # Submit Button for Attendance Update
    update_attendance_button = ctk.CTkButton(scrollable_frame, text="Update Attendance",
                                               command=attendance_insert1)
    update_attendance_button.pack(pady=20)
def attendance_insert1():
        DB_Connect(f"insert into attendance values('{a_attendance_student_id_entry.get()}','{a_attendance_subject_id_entry.get()}','{a_new_attendance_entry.get()}')",0);
        messagebox.showinfo("attendance insertion","attendance inserteed Successfully !");
def mark_insertion(scrollable_frame):
    global i_student_id_entry,i_subject_id_entry,i_new_marks_entry;
    # Clear previous entries
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    ctk.CTkLabel(scrollable_frame, text="Insert Student Marks", font=("Arial", 20)).pack(pady=20)

    ctk.CTkLabel(scrollable_frame, text="Student ID:").pack(pady=5)
    i_student_id_entry = ctk.CTkEntry(scrollable_frame)
    i_student_id_entry.pack(pady=5)

    ctk.CTkLabel(scrollable_frame, text="Subject ID:").pack(pady=5)
    i_subject_id_entry = ctk.CTkEntry(scrollable_frame)
    i_subject_id_entry.pack(pady=5)

    ctk.CTkLabel(scrollable_frame, text="New Marks:").pack(pady=5)
    i_new_marks_entry = ctk.CTkEntry(scrollable_frame)
    i_new_marks_entry.pack(pady=5)

    # Submit Button for Marks insert
    insert_marks_button = ctk.CTkButton(scrollable_frame, text="Update Marks",
                                          command=mark_insert)
    insert_marks_button.pack(pady=20)
def mark_insert():
    DB_Connect(f"insert into mark values('{i_student_id_entry.get()}','{i_subject_id_entry.get()}','{i_new_marks_entry.get()}')",0);
    messagebox.showinfo("mark insertion","mark inserted succesfully")
def show_student_insertion(scrollable_frame):
    # Clear previous entries
    global student_id_entry,student_name_entry,dob_entry,phone_entry,email_entry,dept_id_entry
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    ctk.CTkLabel(scrollable_frame, text="Insert Student Data", font=("Arial", 20)).pack(pady=20)

    # Labels and Entry Fields for Student Data
    ctk.CTkLabel(scrollable_frame, text="Student ID:").pack(pady=5)
    student_id_entry = ctk.CTkEntry(scrollable_frame)
    student_id_entry.pack(pady=5)

    ctk.CTkLabel(scrollable_frame, text="Name:").pack(pady=5)
    student_name_entry = ctk.CTkEntry(scrollable_frame)
    student_name_entry.pack(pady=5)

    ctk.CTkLabel(scrollable_frame, text="Date of Birth (YYYY-MM-DD):").pack(pady=5)
    dob_entry = ctk.CTkEntry(scrollable_frame)
    dob_entry.pack(pady=5)

    ctk.CTkLabel(scrollable_frame, text="Phone Number:").pack(pady=5)
    phone_entry = ctk.CTkEntry(scrollable_frame)
    phone_entry.pack(pady=5)

    ctk.CTkLabel(scrollable_frame, text="Email:").pack(pady=5)
    email_entry = ctk.CTkEntry(scrollable_frame)
    email_entry.pack(pady=5)

    ctk.CTkLabel(scrollable_frame, text="Department ID:").pack(pady=5)
    dept_id_entry = ctk.CTkEntry(scrollable_frame)
    dept_id_entry.pack(pady=5)

    # Submit Button for Student Form
    submit_student_button = ctk.CTkButton(scrollable_frame, text="Submit Student Data",
                                           command=insert_stud_details)
    submit_student_button.pack(pady=20)

def show_faculty_insertion(scrollable_frame):
    global faculty_dept_id_entry,faculty_email_entry,faculty_id_entry,faculty_name_entry,faculty_phone_entry
    # Clear previous entries
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    ctk.CTkLabel(scrollable_frame, text="Insert Faculty Data", font=("Arial", 20)).pack(pady=20)

    # Labels and Entry Fields for Faculty Data
    ctk.CTkLabel(scrollable_frame, text="Faculty ID:").pack(pady=5)
    faculty_id_entry = ctk.CTkEntry(scrollable_frame)
    faculty_id_entry.pack(pady=5)

    ctk.CTkLabel(scrollable_frame, text="Name:").pack(pady=5)
    faculty_name_entry = ctk.CTkEntry(scrollable_frame)
    faculty_name_entry.pack(pady=5)

    ctk.CTkLabel(scrollable_frame, text="Phone Number:").pack(pady=5)
    faculty_phone_entry = ctk.CTkEntry(scrollable_frame)
    faculty_phone_entry.pack(pady=5)

    ctk.CTkLabel(scrollable_frame, text="Email:").pack(pady=5)
    faculty_email_entry = ctk.CTkEntry(scrollable_frame)
    faculty_email_entry.pack(pady=5)

    ctk.CTkLabel(scrollable_frame, text="Department ID:").pack(pady=5)
    faculty_dept_id_entry = ctk.CTkEntry(scrollable_frame)
    faculty_dept_id_entry.pack(pady=5)

    # Submit Button for Faculty Form
    submit_faculty_button = ctk.CTkButton(scrollable_frame, text="Submit Faculty Data",
                                           command=Insert_fac_data)
    submit_faculty_button.pack(pady=20)
def Insert_fac_data():
    DB_Connect(f"insert into faculty values('{faculty_id_entry.get()}','{faculty_name_entry.get()}','{faculty_phone_entry.get()}','{faculty_email_entry.get()}','{faculty_dept_id_entry.get()}')",0)
    messagebox.showinfo("Data Insertion","Data Inserted Successfully !")
    DB_Connect(f"insert into login values('{faculty_id_entry.get()}','4567')",0);
def show_marks_update(scrollable_frame):
    global update_student_id_entry,subject_id_entry,new_marks_entry;
    # Clear previous entries
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    ctk.CTkLabel(scrollable_frame, text="Update Student Marks", font=("Arial", 20)).pack(pady=20)

    ctk.CTkLabel(scrollable_frame, text="Student ID:").pack(pady=5)
    update_student_id_entry = ctk.CTkEntry(scrollable_frame)
    update_student_id_entry.pack(pady=5)

    ctk.CTkLabel(scrollable_frame, text="Subject ID:").pack(pady=5)
    subject_id_entry = ctk.CTkEntry(scrollable_frame)
    subject_id_entry.pack(pady=5)

    ctk.CTkLabel(scrollable_frame, text="New Marks:").pack(pady=5)
    new_marks_entry = ctk.CTkEntry(scrollable_frame)
    new_marks_entry.pack(pady=5)

    # Submit Button for Marks Update
    update_marks_button = ctk.CTkButton(scrollable_frame, text="Update Marks",
                                          command=mark_update)
    update_marks_button.pack(pady=20)
def mark_update():
        DB_Connect(f"update mark set mark='{new_marks_entry.get()}' where s_id='{update_student_id_entry.get()}' and sub_id='{subject_id_entry.get()}'",0);
        messagebox.showinfo("mark updation","mark updated Successfully !");
def show_attendance_update(scrollable_frame):
    global attendance_student_id_entry,attendance_subject_id_entry,new_attendance_entry;
    # Clear previous entries
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    ctk.CTkLabel(scrollable_frame, text="Update Student Attendance", font=("Arial", 20)).pack(pady=20)
    ctk.CTkLabel(scrollable_frame, text="Student ID:").pack(pady=5)
    attendance_student_id_entry = ctk.CTkEntry(scrollable_frame)
    attendance_student_id_entry.pack(pady=5)

    ctk.CTkLabel(scrollable_frame, text="Subject ID:").pack(pady=5)
    attendance_subject_id_entry = ctk.CTkEntry(scrollable_frame)
    attendance_subject_id_entry.pack(pady=5)

    ctk.CTkLabel(scrollable_frame, text="New Attendance:").pack(pady=5)
    new_attendance_entry = ctk.CTkEntry(scrollable_frame)
    new_attendance_entry.pack(pady=5)

    # Submit Button for Attendance Update
    update_attendance_button = ctk.CTkButton(scrollable_frame, text="Update Attendance",
                                               command=attendance_update1)
    update_attendance_button.pack(pady=20)
def attendance_update1():
        DB_Connect(f"update attendance set attendance='{new_attendance_entry.get()}' where s_id='{attendance_student_id_entry.get()}' and sub_id='{attendance_subject_id_entry.get()}'",0);
        messagebox.showinfo("attendance updation","attendance updated Successfully !");
#insertion_to_student
def insert_stud_details():
    DB_Connect(f"insert into student values('{student_id_entry.get()}', '{student_name_entry.get()}', '{dob_entry.get()}', '{phone_entry.get()}', '{email_entry.get()}', '{dept_id_entry.get()}')", 0)  
    DB_Connect(f"insert into login values('{student_id_entry.get()}', '1234')", 0)
    messagebox.showinfo("Data Insertion", "Data Inserted Successfully!")
root = ctk.CTk()
root.title("University Management System")
root.geometry("400x300")

username_label = ctk.CTkLabel(root, text="Username:")
username_label.pack(pady=10)
username_entry = ctk.CTkEntry(root)
username_entry.pack(pady=5)

password_label = ctk.CTkLabel(root, text="Password:")
password_label.pack(pady=10)
password_entry = ctk.CTkEntry(root, show="*")
password_entry.pack(pady=5)

login_button = ctk.CTkButton(root, text="Login", command=login)
login_button.pack(pady=20)

insert_data_button = ctk.CTkButton(root, text="Insert Data", command=show_insertion_forms)
insert_data_button.pack(pady=5)

root.mainloop()