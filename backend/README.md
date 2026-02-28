Todo App Backend

Backend for a Todo App built with Django REST Framework.
Provides APIs for user signup/login and task management (CRUD) with JWT authentication.

Technologies

1.Python 3.10+

2.Django 6.0.1

3.Django REST Framework

4.djangorestframework-simplejwt (JWT auth)

5.SQLite (database)

6.django-cors-headers

Features
1. User Signup

POST /api/register/

Request body:
{ "username": "Juliet", "email": "chi@gmail.com", "password": "mypassword123" }

2. User Login (JWT)

POST /api/login/
Request body:
{ "email": "chi@gmail.com", "password": "mypassword123" }

Returns access & refresh tokens:
{ "refresh": "...", "access": "..." }

3. Task API

GET /api/tasks/ → List user tasks

POST /api/tasks/ → Create task

Requires Authorization: Bearer <access_token>

