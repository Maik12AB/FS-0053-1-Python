
ejecutar:
# 	clear
	python src/p04-area-rectangulo.py

ingresar:
	clear
# 	docker exec -it --user vscode fs-0053-1-dev bash
	docker exec -it --user root fs-0053-1-dev bash

postgres:
	clear
	PGPASSWORD=postgres psql -h postgres -U postgres -d postgres

django-inicio:
	clear
	cd django_inicio && python manage.py runserver 0.0.0.0:8000
