### Python Testing 101

This project is based from flaskr (A Flask tutorial project)


## Setup

You need pipenv in order to install all dependencies to install pipenv via pip

```
pip install pipenv
```

After that using pipenv to create virtual environment

```
cd python-testing-101
pipenv install
```

After virtualenv is created you can enter environment by

```
pipenv shell
```

To start project execute
```
pipenv run flask
```


## Running Test

This test including pytest and coverage package. To running all test case execute

```
pytest
```

To view coverage report execute

```
coverage run -m pytest && coverage report
```