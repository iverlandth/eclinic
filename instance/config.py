import os

try:
    # localhost connection
    database = 'eclinical_dev'
    user = 'postgres'
    password = 'root'
    host = 'localhost'
    port = 5433

except ImportError:
    # production connection
    import urlparse

    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse(os.environ["HEROKU_POSTGRESQL_BRONZE_URL"])
    database = url.path[1:]
    user = url.username
    password = url.password
    host = url.hostname
    port = url.port


SECRET_KEY = 'p9Bv<3Eid9%$i01'
SQLALCHEMY_DATABASE_URI = 'postgres://%s:%s@%s:%s/%s' % (user, password, host, port, database)
