# REST_courses_site
Courses site with RESTfull API

# Installation
```bash
pip3 install -r requirements.txt
cd edu
./manage.py migrate
```
# Usage
```bash
./manage.py runserver
```
for using Celery you must have installed redis in the system.
for starting celery:
```bash
celery -A edu worker -B
```
