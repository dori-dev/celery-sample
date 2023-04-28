from celery.schedules import crontab


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
