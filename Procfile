web: gunicorn manage:app -w 3
worker: rqworker -u $REDIS_URL
