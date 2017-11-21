import logging

from flask import jsonify, make_response
from flask_restful import Resource
from structlog import wrap_logger
from sqlalchemy import create_engine

from config import Config

logger = wrap_logger(logging.getLogger(__name__))


class TestData(Resource):

    """Rest endpoint to provide application service information"""

    @staticmethod
    def get():
        engine = create_engine(Config.RAS_SECURE_MESSAGE_DB_URI)

        with engine.begin() as connection:
            result = connection.execute("SELECT body "
                                        "FROM public.secure_message ")

            data = []
            for row in result:
                data.append(row['body'])

        return make_response(jsonify(data), 200)
