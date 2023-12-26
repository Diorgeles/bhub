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
	@echo "#########################"
	@echo "# Running test database #"
	@echo "#########################"
	docker-compose -f 'docker-compose-database.yaml' up  --remove-orphans -d

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
 
super-user:
	@echo "#######################"
	@echo "#  Create super user  #"
	@echo "#######################"
	docker-compose exec server bash -c "ENV=$(env) python manage.py createsuperuser --username=diorgeles --email=diorgeles@gmail.com --noinput"

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

