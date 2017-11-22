import logging
import os

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from structlog import wrap_logger

from cloud.resources.info import Info
from cloud.resources.drop import DropSecureMessage, DropParty
from cloud.cloud_foundry import ONSCloudFoundry
from logger_config import logger_initial_config

from sqlalchemy import MetaData

metadata = MetaData()


logger_initial_config(service_name='clear_down')
logger = wrap_logger(logging.getLogger(__name__))

# use cf env to extract Cloud Foundry environment
cf = ONSCloudFoundry()

app = Flask(__name__)
api = Api(app)
CORS(app)

logger.info('Starting clear down test ...')

api.add_resource(Info, '/info')
api.add_resource(DropSecureMessage, '/drop/secure_message')
api.add_resource(DropParty, '/drop/party')

DEV_PORT = os.getenv('DEV_PORT', 8080)
app.run(debug=True, host='0.0.0.0', port=int(DEV_PORT))

