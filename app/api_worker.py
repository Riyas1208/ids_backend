# simple example of enqueuing tasks to Redis (RQ)
from redis import Redis
from rq import Queue
from os import getenv

redis_url = getenv('REDIS_URL','redis://localhost:6379/0')
redis_conn = Redis.from_url(redis_url)
q = Queue('default', connection=redis_conn)

def enqueue_task(func, *args, **kwargs):
    return q.enqueue(func, *args, **kwargs)
