Laboratorio 1 - Django (todoproject)

En Windows (CMD), dentro de esta carpeta:
  python -m venv venv
  venv\Scripts\activate
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py runserver          -> http://127.0.0.1:8000/  (lista de tareas)
  python manage.py runserver 8080     -> http://localhost:8080/app/sumar/18/19
                                         http://localhost:8080/app/restar/18/19
                                         http://localhost:8080/app/multiplicar/18/19

db.sqlite3 ya incluye Tarea1, Tarea2 y Tarea3.
