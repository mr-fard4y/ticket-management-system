init_all:
	make init_env

init_env:
	python3 -m pip install pipenv && pipenv install

run_server:
	pipenv run python manage.py runserver

run_tests:
	pipenv run pytest

run_docker:
	make build_docker && make start_docker

build_docker:
	docker-compose build

start_docker:
	docker-compose up

destroy_docker:
	docker-compose down
