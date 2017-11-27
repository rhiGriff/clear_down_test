import os

RAS_SECURE_MESSAGE_DB_URI = os.getenv('RAS_SECURE_MESSAGE_DB_URI', 'postgres://postgres:postgres@localhost:5432/postgres')
RAS_PARTY_DB_URI = os.getenv('RAS_PARTY_DB_URI', 'postgres://postgres:postgres@localhost:5432/postgres')
RAS_COLLECTION_INSTRUMENT_DB_URI = os.getenv('RAS_COLLECTION_INSTRUMENT_DB_URI', 'postgres://postgres:postgres@localhost:5432/postgres')

RM_SAMPLE_SERVICE = os.getenv('RM_SAMPLE_SERVICE', 'postgres://postgres:postgres@localhost:5432/postgres')
RM_SURVEY_SERVICE = os.getenv('RM_SURVEY_SERVICE', 'postgres://postgres:postgres@localhost:5432/postgres')
RM_COLLECTION_EXERCISE = os.getenv('RM_COLLECTION_EXERCISE', 'postgres://postgres:postgres@localhost:5432/postgres')
RM_ACTION_SERVICE = os.getenv('RM_ACTION_SERVICE', 'postgres://postgres:postgres@localhost:5432/postgres')
RM_ACTION_EXPORTER_SERVICE = os.getenv('RM_ACTION_EXPORTER_SERVICE', 'postgres://postgres:postgres@localhost:5432/postgres')
RM_NOTIFY_GATEWAY_SERVICE = os.getenv('RM_NOTIFY_GATEWAY_SERVICE', 'postgres://postgres:postgres@localhost:5432/postgres')
RM_IAC_SERVICE = os.getenv('RM_IAC_SERVICE', 'postgres://postgres:postgres@localhost:5432/postgres')
