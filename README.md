celery -A tasks worker -l INFO
celery -A tasks worker -l INFO --pool=solo --concurrency=1
celery -A tasks worker -l INFO --pool=eventlet --concurrency=500

perfork => CPU-Bound
solo => Whole CPU
eventlet => IO-Bound

use 3 worker and queues for each one

python tasks.py

celery flower -A tasks --broker=amqp://guest:guest@localhost:5672//

celery -A tasks beat
