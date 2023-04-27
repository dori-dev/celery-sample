from time import sleep
from celery import Celery

app = Celery(main='main')
app.config_from_object('conf')


@app.task
def add(x, y):
    sleep(5)
    return x + y


if __name__ == '__main__':
    result = add.delay(5, 3)
    print(result.get())
