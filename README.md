celery -A tasks worker -l INFO
python tasks.py
celery flower -A tasks --broker=amqp://guest:guest@localhost:5672//
