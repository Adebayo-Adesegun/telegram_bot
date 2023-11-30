# Documentation

Simple Telegram Bot Tryout

## Initial Project Setup

- Create a virtual environment for the project
   `python3 -m venv env`

- Activate the virtual environment
   `& .\env\scripts\activate` (Windows)
   `source env/bin/activate` (Linux/Mac)

- Install the required packages
   `pip3 install -r requirements.txt`

- Run migration to create the database
   `python3 manage.py migrate`

- Make migrations for the models
   `python3 manage.py makemigrations`

- Run the project
   `gunicorn -b 0.0.0.0:8443 app:app`
   `gunicorn -b 0.0.0.0:80 app:app --timeout 1000 --log-level debug --worker-class gthread`
# telegram_bot
