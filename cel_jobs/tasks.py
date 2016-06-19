from celery import Celery

celery_app = Celery(
    __name__, backend='amqp://mq:mq@localhost/localhost',
    broker='amqp://mq:mq@localhost/localhost')


@celery_app.task
def add(x, y):
    return x + y
