import psycopg2
from psycopg2 import extras, pool

from malfoy.settings import DB_CONFIG


_pool = None


def init(config=None):
    global _pool
    print('[init]')
    if _pool is not None:
        print('[init] pool already exists')
        return
    if not config:
        config = DB_CONFIG
    print('[init] creating pool')
    print(f"[init]   name: {DB_CONFIG['host'][:17]}, db: {DB_CONFIG['dbname'][:4]}, pass: {DB_CONFIG['password'][:3]}")
    _pool = psycopg2.pool.SimpleConnectionPool(1, 10, **config)


def query(sql, data=None):
    global _pool
    print('   [query]')
    print('   [query] get connection')
    connection = _pool.getconn()
    result = None
    try:
        print('   [query] get cursor')
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        print('   [query] cursor execute')
        cursor.execute(sql, data)
        result = cursor.fetchall()
        print('   [query] close cursor')
        cursor.close()
        connection.commit()
    except psycopg2.Error as e:
        print('   [query] An SQL error occured:', e)
        connection.rollback()
    finally:
        print('   [query] put connection')
        _pool.putconn(connection)
    return result


def close():
    global _pool
    if _pool is not None:
        _pool.close()
        _pool = None
