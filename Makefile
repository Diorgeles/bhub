env=dev
venv=.venv/bin
run:
	@echo "##################"
	@echo "# Running docker #"
	@echo "##################"
	docker-compose up --remove-orphans

rebuild:
	@echo "##################"
	@echo "# Rebuild docker #"
	@echo "##################"
	docker-compose up --remove-orphans --build

run-db:
	@echo "####################"
	@echo "# Running database #"
	@echo "####################"
	docker-compose -f 'docker-compose-database.yaml' up  --remove-orphans -d

down:
	@echo "###########################"
	@echo "# Close docker containers #"
	@echo "###########################"
	docker-compose down

start: local-migrate
	@echo "#######################"
	@echo "# Running application #"
	@echo "#######################"
	ENV=$(env) ./manage.py runserver 0.0.0.0:8000

local-migrate:
	@echo "#####################"
	@echo "# Running migrate #"
	@echo "#####################"
	ENV=$(env) ./manage.py migrate

migrations:
	@echo "#####################"
	@echo "# Running migrate #"
	@echo "#####################"
	ENV=$(env) ./manage.py makemigrations

migrate:
	@echo "#####################"
	@echo "# Running migrate #"
	@echo "#####################"
	docker-compose exec server bash -c "ENV=$(env) ./manage.py migrate"

server-migrations:
	@echo "#####################"
	@echo "# Create migrations #"
	@echo "#####################"
	docker-compose exec server bash -c "ENV=$(env) ./manage.py makemigrations"

exec:
	@echo "#####################"
	@echo "# Connect container #"
	@echo "#####################"
	docker-compose exec server bash

shell:
	@echo "##############"
	@echo "# Call shell #"
	@echo "##############"
	docker-compose exec server bash -c "ENV=$(env) ./manage.py shell"

test:
	@echo "######################"
	@echo "#  Running all test  #"
	@echo "######################"
	ENV=test $(venv)/pytest --no-header -rfE

only:
	@echo "#####################################"
	@echo "#  Running all test with only mark  #"
	@echo "#####################################"
	ENV=test $(venv)/pytest --no-header -rpPfE -m only

break:
	@echo "###############################################"
	@echo "#  Running all test with break and only mark  #"
	@echo "###############################################"
	ENV=test $(venv)/pytest --no-header -s -m only

unit:
	@echo "#######################"
	@echo "#  Running unit test  #"
	@echo "#######################"
	ENV=test $(venv)/pytest --no-header -rfE ./tests/unit

feature:
	@echo "##########################"
	@echo "#  Running feature test  #"
	@echo "##########################"
	ENV=test $(venv)/pytest --no-header -rfE ./tests/feature

cov:
	@echo "######################"
	@echo "#  Running cov test  #"
	@echo "######################"
	ENV=test $(venv)/pytest --cov=. tests/

cov-html:
	@echo "#############################"
	@echo "#  Export cov test to HTML  #"
	@echo "#############################"
	ENV=test $(venv)/pytest --cov --cov-config=pyproject.toml --cov-report html

format:
	@echo "#####################"
	@echo "#  Format all code  #"
	@echo "#####################"
	$(venv)/ruff format .

check: format
	@echo "####################"
	@echo "#  Check all code  #"
	@echo "####################"
	$(venv)/ruff check . --fix

