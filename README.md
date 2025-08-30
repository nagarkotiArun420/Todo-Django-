# ✅ Django To-Do App

A simple and functional **To-Do application built with Django**.  
It provides an intuitive interface to manage daily tasks with **CRUD operations** and status updates.  
The app uses **HTML, CSS, and Bootstrap** for the frontend and Django for the backend.  

--------------------------------------------------------------------------------
🚀 Features
--------------------------------------------------------------------------------
- Add new tasks  
- Update/edit tasks  
- Delete tasks  
- Mark tasks as **done**  
- Undo completed tasks (revert back to pending)  
- Responsive design using Bootstrap  
- Follows **CRUD operations** cleanly  

--------------------------------------------------------------------------------
🛠️ Tech Stack
--------------------------------------------------------------------------------
- **Backend**: Django  
- **Frontend**: HTML, CSS, Bootstrap, Django Templates  
- **Database**: SQLite (default)  
- **IDE**: Visual Studio Code  

--------------------------------------------------------------------------------
⚙️ Installation
--------------------------------------------------------------------------------
# 1. Clone the repository
git clone https://github.com/nagarkotiArun420/Todo-Django-.git
cd Todo-Django

# 2. Create a virtual environment and activate it
python -m venv env
env\Scripts\activate     # Windows
source env/bin/activate  # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver

--------------------------------------------------------------------------------
📂 File Structure
--------------------------------------------------------------------------------
Todo-Django/
│── manage.py
│── db.sqlite3
│── requirements.txt
├── todo/                # Main app (CRUD functionality)
├── templates/           # HTML templates (Bootstrap-based)
├── static/              # CSS/JS files
└── media/ (optional)    # If extended for file uploads

--------------------------------------------------------------------------------
📖 Usage
--------------------------------------------------------------------------------
- Open the app in your browser (http://127.0.0.1:8000).  
- Add tasks from the input form.  
- Edit or delete tasks from the list.  
- Mark tasks as **done** when completed.  
- Undo done tasks if needed.  

--------------------------------------------------------------------------------
🚧 Future Improvements
--------------------------------------------------------------------------------
- Add user authentication (login/registration).  
- Allow task deadlines and reminders.  
- Add task categories (work, personal, etc.).  
- Use PostgreSQL/MySQL for production.  
- Deploy on Heroku or Railway for public access.  

--------------------------------------------------------------------------------
📜 License
--------------------------------------------------------------------------------
This project is **open-source** and free to use.  

--------------------------------------------------------------------------------
📬 Contact
--------------------------------------------------------------------------------
- GitHub: https://github.com/nagarkotiArun420
- Email: nagarkotiarun420@gmail.com
- LinkedIn: https://www.linkedin.com/in/arun-nagarkoti-b53276263/
