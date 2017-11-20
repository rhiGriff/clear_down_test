import json
import logging
import os

from pathlib import Path
from flask import jsonify, make_response
from flask_restful import Resource
from structlog import wrap_logger

logger = wrap_logger(logging.getLogger(__name__))


class Services(Resource):

    """Rest endpoint to provide application service information"""

    @staticmethod
    def get():

        services = json.loads(os.getenv('VCAP_SERVICES'))

        logger.info(services)

        return make_response(jsonify(services), 200)
