from time import sleep
from celery import Celery

app = Celery(main='tasks')
app.config_from_object('conf')


@app.task
def add(x, y):
    # sleep(5)
    return x + y


@app.task
def increase(number):
    return number + 1


@app.task
def success_message():
    return 'Task complete successfully!'


if __name__ == '__main__':
    result = add.signature((5, 6))
    # result.apply_async(link=increase.signature())
    result.apply_async(link=success_message.signature(immutable=True))
