gunicorn --workers $GUNICORN_WORKERS --threads $GUNICORN_THREADS --timeout 60 --access-logfile \
    '-' --error-logfile '-' --bind=0.0.0.0:8000 \
     --chdir=/home/site/wwwroot project.wsgi