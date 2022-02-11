import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerybeat_app.settings')

app = Celery('celerybeat_app', include=['celerybeat_app.tasks'])
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
