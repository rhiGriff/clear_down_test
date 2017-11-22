import os

RAS_SECURE_MESSAGE_DB_URI = os.getenv('RAS_SECURE_MESSAGE_DB_URI', 'postgres://postgres:postgres@localhost:5432/postgres')
RAS_PARTY_DB_URI = os.getenv('RAS_PARTY_DB_URI', 'postgres://postgres:postgres@localhost:5432/postgres')
