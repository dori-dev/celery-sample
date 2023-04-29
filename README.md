# Sample Sample

Sample of using Celery in python.

#

## Celery Worker

```
celery -A tasks worker -l INFO
```

## Run Tasks

```
python tasks.py
```

## Management GUI for Celery

```
celery flower -A tasks --broker=amqp://guest:guest@localhost:5672//
```

## Celery Beat

```
celery -A tasks beat
```

## Use Another Pools

```
celery -A tasks worker -l INFO --pool=solo --concurrency=1
celery -A tasks worker -l INFO --pool=eventlet --concurrency=500
```

`perfork` => CPU-Bound <br>
`solo` => Whole CPU <br>
`eventlet` => IO-Bound <br>

#

## Links

Download Source Code: [Click Here](https://github.com/dori-dev/celery-sample/archive/refs/heads/master.zip)

My Github Account: [Click Here](https://github.com/dori-dev/)
