# from __future__ import absolute_import
# import os
# from celery import Celery
# from django.conf import settings

# # this code copied from manage.py
# # set the default Django settings module for the 'celery' app.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_Demo.settings')

# # you change change the name here
# app = Celery("Project_Demo")

# # read config from Django settings, the CELERY namespace would make celery
# # config keys has `CELERY` prefix
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # load tasks.py in django apps
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

from __future__ import absolute_import, unicode_literals
from django.conf import settings

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_Demo.settings')

app = Celery('Project_Demo')

app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.broker_url = "redis://localhost:6379/0"

# app.conf.beat_schedule = {
#     'add-every-5-seconds': {
#         'task': 'update_rates',
#         'schedule': 5.0
#     },
# }

app.autodiscover_tasks()
