from celery import Celery
from server.settings import CELERY_BROKER_URL


def make_celery():
   celery = Celery(__name__, broker=CELERY_BROKER_URL)
#    celery.conf.update(config.as_dict())
   return celery


celery = make_celery()