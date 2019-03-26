import os


DB_CONFIG = {
    'host': os.environ.get('POSTGRES_HOST'),
    'user': os.environ.get('POSTGRES_USER'),
    'password': os.environ.get('POSTGRES_PASSWORD'),
    'dbname': os.environ.get('POSTGRES_DB'),
    'port': int(os.environ.get('POSTGRES_PORT', '5432')),
}
