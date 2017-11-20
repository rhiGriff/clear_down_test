import logging
import os

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from structlog import wrap_logger

from cloud.resources.info import Info
from cloud.cloud_foundry import ONSCloudFoundry
from logger_config import logger_initial_config

logger_initial_config(service_name='clear_down')
logger = wrap_logger(logging.getLogger(__name__))

# use cf env to extract Cloud Foundry environment
cf = ONSCloudFoundry()


app = Flask(__name__)
api = Api(app)
CORS(app)

if cf.detected:
    logger.info('Cloud Foundry environment identified.', protocol=cf.protocol, database=cf.database())
    app.config['SQLALCHEMY_DATABASE_URI'] = cf.credentials()
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SECURE_MESSAGING_DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432')

app.config['SQLALCHEMY_POOL_SIZE'] = os.getenv('SQLALCHEMY_POOL_SIZE', None)

logger.info('Starting clear down test ...')

api.add_resource(Info, '/info')

DEV_PORT = os.getenv('DEV_PORT', 8080)
app.run(debug=True, host='0.0.0.0', port=int(DEV_PORT))