import logging
import config

from flask_restful import Resource
from structlog import wrap_logger
from sqlalchemy import create_engine, MetaData

logger = wrap_logger(logging.getLogger(__name__))


class DropSecureMessage(Resource):

    @staticmethod
    def post():

        engine = create_engine(config.RAS_SECURE_MESSAGE_DB_URI)
        metadata = MetaData(bind=engine, reflect=True)
        # print(metadata.__dict__)
        for t in metadata.sorted_tables:
            print(t)


class DropParty(Resource):

    @staticmethod
    def post():

        engine = create_engine(config.RAS_PARTY_DB_URI)
        metadata = MetaData(bind=engine, reflect=True, schema='partysvc')
        for t in metadata.sorted_tables:
            print(t)
            # metadata.drop_all()