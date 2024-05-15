SECRET_KEY = 'capitaoamerica.'

SQLALCHEMY_DATABASE_URI = \
    '{dbms}://{username}:{password}@{server}:{port}/{database}'.format(
        dbms='mysql+mysqlconnector',
        username='root',
        password='admin',
        server='localhost',
        port='3306',
        database='parkassistent'
)