# ALX Travel App

This project is part of the ALX Software Engineering track.

## Features
- Django backend with REST Framework
- MySQL database
- Swagger API docs at `/swagger/`
- Listings app for property management
- CORS enabled
- Environment variable configuration using django-environ

## Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/garisonmike/alx_travel_app.git
   cd alx_travel_app
2.Create a virtual environment and install requirements:

python -m venv venv
.\venv\Scripts\activate
pip install -r requirement.txt


3.Configure .env with your database credentials.

4.Run migrations and start the server:

python manage.py migrate
python manage.py runserver


5.Visit:

Swagger Docs: http://127.0.0.1:8000/swagger/

Listings API: http://127.0.0.1:8000/listings/