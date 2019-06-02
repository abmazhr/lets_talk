from os import getenv

USER_MANAGEMENT_SERVICE_HOST = getenv('USER_MANAGEMENT_SERVICE_HOST', 'localhost')
USER_MANAGEMENT_SERVICE_PORT = int(getenv('USER_MANAGEMENT_SERVICE_PORT', 3000))

BIDIRECTIONAL_COMMUNICATION_SERVICE_HOST = getenv('BIDIRECTIONAL_COMMUNICATION_SERVICE_HOST', 'localhost')
BIDIRECTIONAL_COMMUNICATION_SERVICE_PORT = int(getenv('BIDIRECTIONAL_COMMUNICATION_SERVICE_PORT', 3001))