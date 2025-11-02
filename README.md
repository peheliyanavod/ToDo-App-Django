# ✅ Django To-Do Application

A simple yet powerful **To-Do List Web Application** built with **Django**.  
This project allows users to efficiently manage their daily tasks — including creating, updating, marking as completed, and deleting tasks — through a clean and responsive interface.

> “Plan your day, organize your goals, and stay productive.”

---

## 🧠 Overview

The **Django To-Do App** demonstrates essential CRUD (Create, Read, Update, Delete) operations using Django’s Model-View-Template (MVT) architecture.  
It’s ideal for beginners and developers looking to understand Django fundamentals while building a practical productivity tool.

---

## 🚀 Features

✅ Add new tasks easily  
✅ View all existing tasks  
✅ Update or edit tasks  
✅ Mark tasks as completed  
✅ Delete tasks with one click  
✅ Responsive and user-friendly UI  
✅ Database-driven task management  
✅ Automatic timestamps for created and updated tasks  

---

## 🛠️ Tech Stack

### ⚙️ Backend
- **Python**
- **Django**

### 🖥️ Frontend
- **HTML5**
- **CSS3**
- **Bootstrap 5** (optional, for styling)

### 🗄️ Database
- **SQLite3** (default Django database)


---

## 🧩 How It Works

1. **Models:** Define the Task model with fields such as `title`, `description`, `date`, `time`, and `status`.  
2. **Views:** Handle logic for listing, creating, updating, and deleting tasks.  
3. **Templates:** Use Django’s templating engine to display dynamic content in HTML.  
4. **URLs:** Map endpoints to corresponding views (e.g., `/`, `/add/`, `/update/<id>/`, `/delete/<id>/`).  
5. **Forms:** Use Django forms for input validation and handling.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/django-todo-app.git
cd django-todo-app
```
2️⃣ Create and activate a virtual environment
```bash
Copy code
python -m venv venv
venv\Scripts\activate      # For Windows
```
# OR
```
source venv/bin/activate   # For macOS/Linux
```
3️⃣ Install dependencies
```bash

pip install django
```
4️⃣ Run database migrations
```bash
Copy code
python manage.py makemigrations
python manage.py migrate
```
5️⃣ Run the development server
```bash
Copy code
python manage.py runserver
```
Then visit 👉 http://127.0.0.1:8000


🧮 Example Model (Task)
python
```
Copy code
from django.utils import timezone
from django.db import models

class Task(models.Model):
    task_id = models.AutoField(primary_key=True, unique=True, null=False)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

---

### 🔮 Future Enhancements
🔐 Add user authentication and login/logout

📱 Make it fully responsive with a mobile-friendly layout

🗓️ Add deadlines and reminders

📊 Implement progress tracking with charts

☁️ Deploy on Render, Railway, or Heroku

### 👨‍💻 Author
Peheliya Dhanuka Navod
Software Engineering Undergraduate | University of Kelaniya

📧 Email: hwpeheliya@gmail.com

🌐 Portfolio: https://react-portfolio-gray-chi.vercel.app

💼 LinkedIn: linkedin.com/in/peheliya-danuka

✍️ Medium: medium.com/@hwpeheliya


⭐ If you found this project helpful, please give it a star!
