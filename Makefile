init_all:
	make init_env

init_env:
	python3 -m pip install pipenv && pipenv install

run_server:
	pipenv run python manage.py runserver

run_tests:
	pipenv run pytest
