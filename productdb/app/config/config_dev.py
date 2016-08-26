config = {
    'DOMAIN': {},
    'XML': False,
    'JSON': True,
    'DEBUG': True,

    'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
    'ITEM_METHODS': ['GET', 'PATCH', 'DELETE'],

    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,

    # Skip these if your db has no auth. But it really should.
    #MONGO_USERNAME = '<your username>'
    #MONGO_PASSWORD = '<your password>'

    'MONGO_DBNAME': 'products',
}