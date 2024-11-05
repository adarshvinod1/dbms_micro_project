# CollegeManagement
![developer](https://img.shields.io/badge/Developed%20By%20%3A-Adarsh%20Vinod,%20Ayush%20Madhavan,%20Dinil%20PS-red)
---
## Screenshots
### LoginPage
![loginpage](https://github.com/user-attachments/assets/81816daf-ed0f-401f-82ea-aca0c2ab608b)
![Screenshot 2024-11-05 191829](https://github.com/user-attachments/assets/5bcf0758-ea07-4306-bb50-42e5ba192f38)
![Screenshot 2024-11-05 191918](https://github.com/user-attachments/assets/da04a817-d2da-4ce2-b9dc-66ac11885551)
### Insert data dashboard
![Screenshot 2024-11-05 191553](https://github.com/user-attachments/assets/9dc26d39-c8fd-4b35-8c1a-773e5d280ab4)
![Screenshot 2024-11-05 191604](https://github.com/user-attachments/assets/22c3109a-79f9-412a-9b3c-ea996ea15327)
![Screenshot 2024-11-05 191618](https://github.com/user-attachments/assets/95148200-763a-4a93-a8dc-e6b5ee8a76c6)
![Screenshot 2024-11-05 191631](https://github.com/user-attachments/assets/648f7b32-1e94-4023-afef-3b06d23eddee)
![Screenshot 2024-11-05 191643](https://github.com/user-attachments/assets/d484a7b1-3b50-4280-a1e3-66041936e780)
### Student details dashboard
![Screenshot 2024-11-02 091626 1](https://github.com/user-attachments/assets/aee39b4b-a9e3-4a32-b6d2-9998d524032b)
### Faculty details dashboard
![Screenshot 2024-11-05 192032](https://github.com/user-attachments/assets/436f8488-c2c7-4861-ad69-c643ef61677b)
![Screenshot 2024-11-05 192048](https://github.com/user-attachments/assets/b8fb655b-9e71-4ee4-8b72-fd17e2aa89e0)
![Screenshot 2024-11-05 192058](https://github.com/user-attachments/assets/1e80d544-88e1-4c5d-875e-9daf9a98b3f2)
![Screenshot 2024-11-05 192106](https://github.com/user-attachments/assets/d4007532-82e9-48d9-93f1-f5235247b8f6)
![Screenshot 2024-11-05 192115](https://github.com/user-attachments/assets/9fe68a52-5750-4fa9-bf1c-cf1b4fcfbdd4)

---

## Functions
### Student
First student will take admission/signup.
When their account is approved by admin, only then the student can access their dashboard.
After account approval by admin the student can view their details like marks,attendance.
Student can't view attendance of other student.
Student can't alter any details, they can only view.

### Faculty
Admin registers a faculty 
Faculty can enter the marks and attendance of the students
They can also update the marks and attendance
Faculty cant alter their details that can only be done through the admin
### Admin
Admin enters the admin portal 
Admin can register new students and faculty
Admin can also remove the students and faculty 
Admin has no acess to the student or faculty portal 

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
