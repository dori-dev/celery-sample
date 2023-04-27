from time import sleep
from celery import Celery

app = Celery(
    main='add',
    broker='amqp://localhost',
)


@app.task
def add(x, y):
    sleep(15)
    return x + y


if __name__ == '__main__':
    add.delay(5, 3)
