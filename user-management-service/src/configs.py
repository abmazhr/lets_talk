from os import getenv

SERVICE_PORT = int(getenv('SERVICE_PORT', 3000))
SERVICE_HOST = getenv('SERVICE_HOST', '0.0.0.0')

MONGODB_HOST = getenv('MONGODB_HOST', 'localhost')
MONGODB_PORT = int(getenv('MONGODB_PORT', 27017))
