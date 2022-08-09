import os

from celery import Celery

# Set the default Django settings module for the 'celery_module' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')

app = Celery('library')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery_module-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'auto_delete_otp':{
        'task':'customer.tasks.delete_otp',
        'schedule': 3*60

    }
}
# Load task modules from all registered Django apps.
app.autodiscover_tasks()

