run:
	python3 manage.py runserver 7000


shell:
	pipenv shell

migrate:
	python3 manage.py makemigrations && python3 manage.py migrate