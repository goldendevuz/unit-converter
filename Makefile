gen-env:
	python3 -m venv env && . env/bin/activate
migrate:
	python3 manage.py migrate
run:
	python3 manage.py runserver 8000
i:
	pip install -r requirements.txt
freeze:
	pip freeze > requirements.txt