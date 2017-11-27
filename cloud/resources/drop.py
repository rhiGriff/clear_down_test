import logging
import config

from flask_restful import Resource
from structlog import wrap_logger
from sqlalchemy import create_engine, MetaData

logger = wrap_logger(logging.getLogger(__name__))


class DropSecureMessage(Resource):

    @staticmethod
    def post():

        try:
            engine = create_engine(config.RAS_SECURE_MESSAGE_DB_URI)
            logger.info('Deleting Secure Message database')
            metadata = MetaData(bind=engine, reflect=True)
            # print(metadata.__dict__)
            for t in metadata.sorted_tables:
                print(t)

            # metadata.drop_all()
            return 200
        except Exception as e:
            logger.error('Failed to delete Secure Message database', error=e)


class DropParty(Resource):

    @staticmethod
    def post():

        try:
            engine = create_engine(config.RAS_PARTY_DB_URI)
            logger.info('Deleting Party Database')
            metadata = MetaData(bind=engine, reflect=True, schema='partysvc')
            for t in metadata.sorted_tables:
                print(t)

            # metadata.drop_all()
            return 200
        except Exception as e:
            logger.error('Failed to delete Party database', error=e)


class DropCollectionInstrument(Resource):

    @staticmethod
    def post():

        try:
            engine = create_engine(config.RAS_COLLECTION_INSTRUMENT_DB_URI)
            logger.info('Deleting Collection Instrument Database')
            # TODO: Find the correct schema
            metadata = MetaData(bind=engine, reflect=True, schema='')
            for t in metadata.sorted_tables:
                print(t)

            # metadata.drop_all()
            return 200
        except Exception as e:
            logger.error('Failed to delete Collection Instrument database', error=e)


class DropSample(Resource):

    @staticmethod
    def post():

        try:
            engine = create_engine(config.RM_SAMPLE_SERVICE)
            logger.info('Deleting Sample Database')
            metadata = MetaData(bind=engine, reflect=True, schema='sample')
            for t in metadata.sorted_tables:
                print(t)

            # metadata.drop_all()
            return 200
        except Exception as e:
            logger.error('Failed to delete Sample Database', error=e)


class DropCase(Resource):

    @staticmethod
    def post():

        try:
            engine = create_engine(config.RM_SURVEY_SERVICE)
            logger.info('Deleting Case Database')
            metadata = MetaData(bind=engine, reflect=True, schema='casesvc')
            for t in metadata.sorted_tables:
                print(t)

            # metadata.drop_all()
            return 200
        except Exception as e:
            logger.error('Failed to delete Case Database', error=e)


class DropCollectionExercise(Resource):

    @staticmethod
    def post():

        try:
            engine = create_engine(config.RM_COLLECTION_EXERCISE)
            logger.info('Deleting Collection Exercise Database')
            metadata = MetaData(bind=engine, reflect=True, schema='collectionexercise')
            for t in metadata.sorted_tables:
                print(t)

            # metadata.drop_all()
            return 200
        except Exception as e:
            logger.error('Failed to delete Collection Exercise Database', error=e)


class DropAction(Resource):

    @staticmethod
    def post():

        try:
            engine = create_engine(config.RM_ACTION_SERVICE)
            logger.info('Deleting Action Database')
            metadata = MetaData(bind=engine, reflect=True, schema='action')
            for t in metadata.sorted_tables:
                print(t)

            # metadata.drop_all()
            return 200
        except Exception as e:
            logger.error('Failed to delete Action Database', error=e)


class DropActionExporter(Resource):

    @staticmethod
    def post():

        try:
            engine = create_engine(config.RM_ACTION_EXPORTER_SERVICE)
            logger.info('Deleting Action Exporter Database')
            metadata = MetaData(bind=engine, reflect=True, schema='actionexporter')
            for t in metadata.sorted_tables:
                print(t)

            # metadata.drop_all()
            return 200
        except Exception as e:
            logger.error('Failed to delete Action Exporter Database', error=e)
