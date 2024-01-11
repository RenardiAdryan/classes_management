# Class Management Project
## Application Data
- Users
- - School admin staff who log into this app
- Classes
- - A class must have one teacher
- - A class can have one or many students
- Teachers
- - A teacher can have none or many classes
- Students
- - A student can belong to none or one class
 
## Application Flow
-  a login page
-  once logged in, the user can list/create/edit/delete Classrooms, Teachers and Students.
-  the user can assign teachers and students to classrooms
-  the user can download a PDF file that lists all the Classrooms with the names of Teachers and Students in them.

## Tech Stack
1. Django
2. Tailwind CSS
3. Javascript
4. Postgress Database
5. Docker

## Tutorial First RUN
### Setup Database.
1. Go to docker/only_database
2. docker compose up --build
### Setup App.
1. Create Python VENV
2. Install pkg in requirements.txt -> pip install -r requirements.txt
3. Go to directory that has manage.py in it.
4. python manage.py migrate
5. python manage.py runserver
### ENV File Example. (Create env file beside manage.py file)
- ALLOWED_HOSTS=localhost,127.0.0.1,143.198.54.56,app.localhost
- DB_ENGINE=django.db.backends.postgresql
- DB_NAME=clasesManagement
- DB_USER=renardi
- DB_PASS=test
- DB_HOST=127.0.0.1
- DB_PORT=5433
- PARENT_HOST=localhost:8000
- SITE_ID=2
- PARENT_HOST=localhost:8000
- SECRET_KEY=django-insecure-k@!av=#$4b6^@vqd$ovvf^o2w@)&%k36px@4rbk0ab+l$xkml)
- CSRF_TRUSTED_ORIGINS=http://localhost:8000,http://app.localhost:8000
### Demo Video
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/1AgfD2O2kww/0.jpg)](http://www.youtube.com/watch?v=1AgfD2O2kww)


