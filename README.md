Django_test
===========

My first "hello world" repo to establish a python django framework

Test with python 3.10 + django 5.2.9

## Install prerequisites

```bash
pip install -r requirements.txt
```

## Start the web app

```bash
python manage.py runserver
```

Then the app can be accessed through the port `8000` of the `localhost`

## Project structure

```
.
├── article/           # Django app containing views/templates/static assets
├── django_test/       # Project settings and URL routing
├── static/            # Static CSS file and image files
├── templates/         # HTML files for UI design
├── manage.py          # Django management utility
├── requirements.in    # Python dependencies
├── requirements.txt   # Python dependencies with specific version details
├── storage.db         # sqlite database file
├── LICENSE
└── README.md
```