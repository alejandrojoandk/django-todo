# Django To Do Project

## Setup

1. Clone the repository:

  ~git clone https://github.com/alejandrojoandk/django-todo.git
  
  ~cd django-todo

2. Create a virtual environment:

  ~python -m venv venv

3. Install dependencies:

  ~pip install -r requirements.txt

4. Apply migrations(No need to makemigrations because its a small project with one table):

  ~cd todo_list
  ~python manage.py migrate

5. Run the development server:

  ~python manage.py runserver
  ~You can now access the project at http://127.0.0.1:8000/.

Requirements

  ~Python 3.x
  ~Django (included in requirements.txt)
