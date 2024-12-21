-------------------------------------School Fees Management System----------------------------------------------
 

Overview

This is a School Fees Management System built using Django. It includes modules for managing students,
fee categories, and fee payments. Administrators can perform CRUD operations and view a dashboard with
financial insights.

Models

1. AdminModel:
- Fields: name, username, email, password, dob, signup_date.
- Represents administrators who manage the system.
2. Student:
- Fields: first_name, last_name, class_name, roll_number, email.
- Represents students with their basic details.
3. FeeCategory:
- Fields: name, fee_type, amount.
- Represents different types of fees (e.g., tuition, library).
4. StudentFees:
- Fields: student, fee_category, status, due_date, paid_date, amount_paid.
- Represents the fee payment status of students.

Key Features

1. Admin Registration and Login:
- Secure login using hashed passwords.
- Session management for authenticated users.
2. Student Management:
- Add, update, delete, and view students.
3. Fee Management:
- Add, update, delete, and view fee categories.
- Assign fees to students and track payment status.
4. Dashboard:
- View total fees collected, outstanding fees, and recent payments.
- Highlight students with due payments.

Technologies Used

1. Django Framework
2. SQLite (default Django database)
3. HTML, CSS, Bootstrap for frontend
4. Python 3.x

Setup Instructions

1. Clone the repository.
2. Navigate to the project directory.
3. Install dependencies using `pip install -r requirements.txt`.
4. Run migrations with `python manage.py migrate`.
5. Start the development server using `python manage.py runserver`.
6. Access the application at `http://127.0.0.1:8000/`.


