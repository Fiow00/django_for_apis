# README.md

# Django for APIs

A sample Django project demonstrating how to build RESTful APIs using Django REST Framework. This project includes example apps for books, todos, posts, and user authentication, with endpoints for CRUD operations and API documentation via drf-spectacular.

## Features

- Modular apps: Books, Todos, Posts, Accounts
- RESTful API endpoints with [Django REST Framework](https://www.django-rest-framework.org/)
- Token and session authentication with [dj-rest-auth](https://dj-rest-auth.readthedocs.io/)
- User registration and authentication
- API schema and documentation with [drf-spectacular](https://drf-spectacular.readthedocs.io/)
- CORS support for frontend integration

## Project Structure

```
├── accounts/
├── apis/
├── books/
├── posts/
├── todos/
├── django_for_apis/
├── manage.py
├── requirements.txt
├── schema.yml
└── db.sqlite3
```

## Setup

1. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

2. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

3. **Create a superuser (optional):**
    ```sh
    python manage.py createsuperuser
    ```

4. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

5. **Access API docs:**
    - Swagger UI: [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)
    - Redoc: [http://localhost:8000/api/schema/redoc/](http://localhost:8000/api/schema/redoc/)

## API Endpoints

- `/api/books/` — List and create books
- `/api/todos/` — List and create todos
- `/api/posts/` — CRUD for posts
- `/api/users/` — User management (admin only)
- `/api/dj-rest-auth/` — Authentication endpoints
