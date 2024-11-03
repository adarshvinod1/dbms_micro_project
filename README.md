# CollegeManagement
![developer](https://img.shields.io/badge/Developed%20By%20%3A-Adarsh%20Vinod,%20Ayush%20Madhavan,%20Dinil%20PS-red)
---
## Screenshots
### LoginPage
![loginpage](https://github.com/user-attachments/assets/81816daf-ed0f-401f-82ea-aca0c2ab608b)
### Insert data dashboard
![Screenshot 2024-11-02 181222 1](https://github.com/user-attachments/assets/75e50943-f015-4897-ba0d-03dbe32aea4f)
![Screenshot 2024-11-02 181233 1](https://github.com/user-attachments/assets/3a9b17da-f5e3-464c-8ee7-fcc1012cbd62)
![Screenshot 2024-11-02 181248 1](https://github.com/user-attachments/assets/6534a0b6-b0fd-4b25-adbf-0a005f616cf7)
![Screenshot 2024-11-02 181302 1](https://github.com/user-attachments/assets/c3a2c9ec-8ff1-4271-8516-6d3e43b38992)
![Screenshot 2024-11-02 181322 1](https://github.com/user-attachments/assets/0cf7ae02-1896-4d08-aa01-d4407a8a9a2b)
![Screenshot 2024-11-02 181335 1](https://github.com/user-attachments/assets/13e91580-f922-46a3-8713-9f05611d225c)
![Screenshot 2024-11-02 181353 1](https://github.com/user-attachments/assets/c1e20856-2ad9-430b-b33f-5253b8991007)
### Student details dashboard
![Screenshot 2024-11-02 091626 1](https://github.com/user-attachments/assets/aee39b4b-a9e3-4a32-b6d2-9998d524032b)
### Faculty details dashboard
![Screenshot 2024-11-02 182056 1](https://github.com/user-attachments/assets/47315ca3-8b2a-4a38-bc7d-a0181bd80ba6)
---

## Functions
### Student
First student will take admission/signup.
When their account is approved by admin, only then the student can access their dashboard.
After account approval by admin the student can view their details like marks,attendance.
Student can't view attendance of other student.
Student can't alter any details, they can only view.

### Faculty
Admin enters the details of the faculty only after that the faculty can access their dashboard.
Faculty can only view their dashboard, student marks and attendance is updated via admin.

### Admin
First admin will signup for a account.
They can insert student data including their marks and attendance. 
They can also insert faculity data.
They can update student marks and attendance.

## Drawbacks
- Dependent on Tkinder: Limited visual customization.
- Static Passwords: All students use 1234 and all faculity use 4567 as passwords,making it easy for unauthorized access and reducing security.

## Technologies Used
- Python 3.x
- MySQL Server
- Libraries:
- ```
    - `CustomTkinter` for GUI
    - `mysql-connector-python` for database interaction

## Installation
1. Ensure you have Python 3.x installed.
2. Set up a MySQL database and create the required tables (`student`, `faculty`, `department`, `login`, `attendance`, `mark`, `subject`).
3. Install the required Python packages:
    -pip install customtkinter
    -pip install customtkinter mysql-connector-python

## Disclaimer
This project is developed for demo purpose and it's not supposed to be used in real application.

## Feedback
Any suggestion and feedback is welcome. You can mail us on
- Ayush : ayushmadhavan183@gmail.com
- Adarsh: adarshvnd2@gmail.com
- Dinil: dinilps2004@gmail.com
