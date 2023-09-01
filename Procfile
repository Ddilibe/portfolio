release: echo "yes" | python manage.py collectstatic
web: gunicorn core.wsgi --log-file -
