Django_test
===========

My first "hello world" repo to establish a python django framework

Test with python 3.10 + django 5.2.9

## Install prerequisites

```bash
pip install -r requirements.in
```

Alternatively, you can install the packages with `uv` tool.

```bash
uv add -r requirements.in
```

## Start the web app

```bash
python manage.py runserver
```

In case you are using `uv` tool, launch the app with

```bash
uv run manage.py runserver
```

Then the app can be accessed through the port `8000` of the `localhost`

## Test the app

Run the command to validate the test

```bash
python manage.py test article
```

## Project structure

```
.
├── article/           # Django app containing views/templates/static assets
├── django_test/       # Project settings and URL routing
├── static/            # Static CSS file and image files
├── templates/         # HTML files for UI design
├── manage.py          # Django management utility
├── pyproject.toml     # Python project configuration file declaring how the project is built
├── requirements.in    # Python dependencies
├── requirements.txt   # Python dependencies with specific version details
├── storage.db         # sqlite database file
├── uv.lock            # Pin the exact dependency versions, generated from `pyproject.toml`
├── LICENSE
└── README.md
```
