from celery.schedules import crontab
from kombu import Queue, Exchange


# urls
broker_url = 'amqp://localhost'
result_backend = 'rpc://'

# timezone
enable_utc = True
timezone = 'Asia/Tehran'

# serializer
task_serializer = 'json'
result_serializer = 'json'

# schedules
beat_schedule = {
    'call_add_every_one_minute': {
        'task': 'tasks.add',
        'schedule': crontab(minute='*/1'),
        'args': (143, 546),
    },
}

# queues
default_exchange = Exchange('default', type='direct')
success_exchange = Exchange('success', type='direct')
add_exchange = Exchange('add', type='direct')
task_queues = (
    Queue('default', default_exchange, routing_key='default'),
    Queue('success', success_exchange, routing_key='success'),
    Queue('add-queue', add_exchange, routing_key='add'),
)

# default queue
task_default_queue = 'default'
task_default_exchange = 'default'
task_default_routing_key = 'default'

# task routes
task_routes = {
    'tasks.add': {
        'queue': 'add-queue',
    },
    'tasks.success*': {
        'queue': 'success',
    },
}
