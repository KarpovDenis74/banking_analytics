from celery.schedules import crontab
import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banking_analytics.settings')

app = Celery('banking_analytics')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    """Запускать каждый час """
    'add-currency': {
        'task': 'apps.currency.tasks.set_currency',
        'schedule': crontab(minute=0, hour='*/1'),
    },
}
