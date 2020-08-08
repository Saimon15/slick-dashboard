import time

from server.tasks import celery


@celery.task()
def process_data():
   time.sleep(60)