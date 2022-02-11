from datetime import datetime
from random import randint

from celerybeat_app.celery import app


@app.task
def make_txt():
    with open(f"media/{str(datetime.utcnow())}_file.txt", "w") as f:
        pass
