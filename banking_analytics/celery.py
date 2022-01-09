import os

from celery import Celery
from celery.schedules import crontab

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
    """
        Запрос курсов
    """
    'add-currency': {
        'task': 'apps.currency.tasks.get_currency',
        'schedule': crontab(minute=4, hour='*/1'),
    },
    """
        Обновление балансовых счетов
    """
    'add-balance-accounts': {
        'task': 'apps.banks.tasks.get_accounts',
        'schedule': crontab(minute=1,
                            hour=1,
                            day_of_month='1,10,20',
                            month_of_year='*/1'),
    },
    """
        Обновление списка регионов
    """
    'add-regions': {
        'task': 'apps.banks.tasks.get_regions',
        'schedule': crontab(minute=1,
                            hour=2,
                            day_of_month='1,2,27',
                            month_of_year='*/1'),
    },
    """
        Обновление справочников БИК
    """
    'add-bics': {
        'task': 'apps.banks.tasks.get_bics',
        'schedule': crontab(minute=1,
                            hour=3,
                            day_of_month='3,4,28',
                            month_of_year='*/1'),
    },
}
