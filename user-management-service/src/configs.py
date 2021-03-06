from os import getenv

SERVICE_RUNTIME = getenv('SERVICE_RUNTIME', 'locally')
SERVICE_PORT = int(getenv('SERVICE_PORT', 3000))
SERVICE_HOST = getenv('SERVICE_HOST', '0.0.0.0')

MONGODB_HOST = getenv('MONGODB_HOST', 'localhost')
MONGODB_PORT = int(getenv('MONGODB_PORT', 27017))
MONGODB_NAME = getenv('MONGODB_NAME', 'users_management')
