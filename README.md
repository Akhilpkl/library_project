# 📚 library_project

A simple web-based Library Management System built using **Flask (Python)** and **MySQL**. This project allows users to manage books and library members efficiently through a user-friendly web interface.

---

## 🔧 Features

- 📝 View all books  
- ➕ Add new books  
- 👥 View library members  
- ➕ Add new members  

---

## 💻 Tech Stack

- **Backend**: Python (Flask)  
- **Frontend**: HTML (Jinja2 templates)  
- **Database**: MySQL (with PyMySQL connector)  

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/library_project.git
cd library_project
```

### 2. Install Required Python Packages

Make sure you have Python installed (version 3.8+ recommended):

```bash
pip install flask pymysql cryptography
```

### 3. Set Up MySQL Database

Create a MySQL database and the required tables:

```sql
CREATE DATABASE library_db;

USE library_db;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL
);

CREATE TABLE members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);
```

### 4. Update Database Credentials

In your `app.py`, update the following line with your MySQL password:

```python
pymysql.connect(host='localhost', user='root', password='your_password', database='library_db')
```

---

### 🏃‍♂️ Run the App

```bash
python app.py
```

Then open your browser and visit:  
[http://localhost:5000](http://localhost:5000)

---

## 📂 Project Structure

```
library_project/
│
├── templates/
│   ├── home.html
│   ├── add_book.html
│   ├── members.html
│   └── add_member.html
│
├── app.py
└── README.md
```

---

## 📌 Future Improvements (Optional)

- 🛠 Edit/Delete functionality for books and members  
- 🔐 Member login system  
- 📕 Book issue and return tracking  
- 🔍 Search functionality  

---

## 👨‍💻 Author

**Akhil shaji**
