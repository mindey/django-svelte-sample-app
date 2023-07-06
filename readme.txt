Origin:
- https://web.archive.org/web/20230130025107/https://dev.to/besil/my-django-svelte-setup-for-fullstack-development-3an8
Docker:
- https://web.archive.org/web/20230706003231/https://dev.to/besil/my-django-dev-utilities-4p2e


# Start

python3 -m venv .venv
. .venv/bin/activate

pip install poetry
poetry install

DJANGO_DEBUG=ON poetry run python manage.py migrate
DJANGO_DEBUG=ON poetry run python manage.py createsuperuser
HOST=my.host.name DJANGO_DEBUG=ON poetry run python manage.py runserver 0.0.0.0:8000


cd frontend
npm install
npm run dev

# check:

http://0.0.0.0:8000
http://0.0.0.0:8000/api/greet


# then:
npm run build
poetry run python manage.py collectstatic
HOST=my.host.name poetry run gunicorn backend.wsgi --bind 0.0.0.0:8000
