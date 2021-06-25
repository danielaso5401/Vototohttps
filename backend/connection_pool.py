import time
from psycopg2.pool import SimpleConnectionPool
from contextlib import contextmanager

dbConnection = "dbname='sistema_votacionV2' user='postgres' host='localhost' password='postgres'"
connectionpool = SimpleConnectionPool(1,10,dsn=dbConnection)