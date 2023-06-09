from time import sleep
from celery import Celery, signals, chain, group

app = Celery(main='tasks')
app.config_from_object('conf')


@app.task
def add(x, y):
    sleep(1)
    return x + y


@app.task
def increase(number):
    return number + 1


@app.task
def success():
    return "Task complete successfully!"


@app.task
def success_message(number):
    return f'The result is {number}'


@signals.task_success.connect(sender=add)
def success_add(sender, result, **kwargs):
    print(f'success sum: {result}')


# @signals.task_prerun.connect
# def show(sender=None, **kwargs):
#     print(sender)
#     print(kwargs)


# @signals.task_postrun.connect
# def show_info(sender, **kwargs):
#     print(sender.request.task)
#     print(sender.request.delivery_info)


if __name__ == '__main__':
    # simple usage
    result = add.delay(2, 3)
    print(result.get())
    # signature
    result = add.signature((5, 6))
    result.apply_async(link=increase.signature())
    result.apply_async(link=success.signature(immutable=True))
    # chain
    result = chain(add.s(3, 9), increase.s(), success_message.s())
    print(result().parent.parent.get())
    print(result().get())
    # group
    result = group(add.s(1, 2), add.s(5, 9), add.s(9, 9)).apply_async()
    print(result.ready())
    print(result.get())
    print(result.ready())
