# HardikAjmani_emailchaser_backend_trial

Steps to setup
- cd into the root folder
- `python3 -m venv venv `
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `cd emailchaser`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py runserver`
- head to http://127.0.0.1:8000/