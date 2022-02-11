from random import randint

from celerybeat_app.celery import app


@app.task
def make_txt():
    with open(f"media/{randint(1, 1000)}_file.txt", "w") as f:
        pass
