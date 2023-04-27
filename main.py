from time import sleep
from celery import Celery

app = Celery(
    main='main',
    backend='rpc://',
    broker='amqp://localhost',
)


@app.task
def add(x, y):
    sleep(5)
    return x + y


if __name__ == '__main__':
    result = add.delay(5, 3)
    # result.ready()
    print(result.get())
