import logging
import os

logger = logging.getLogger(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

env = os.getenv('ENV')
try:
    if env == 'PRODUCTION':
        from .production import ProductionConfig as BaseConfig

        logging.info('Production config loaded.')
    else:
        from .default import Config as BaseConfig

        logging.info('default config loaded.')
except ImportError:
    logging.warning('Loading config for %s environment failed, use default config instead.', env or 'unspecified')
    from .default import Config as BaseConfig


class Config:
    # DEBUG
    DEBUG = BaseConfig.get('DEBUG')
    MONGO_URI = BaseConfig.get('MONGO_URI')
    SQLALCHEMY_DATABASE_URI = BaseConfig.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_BINDS = BaseConfig.get('SQLALCHEMY_BINDS')
    TIMEOUT = (1, 5)
    # 日志设置
    LOG_PATH = BaseConfig.get('LOG_PATH')
    LOG_LEVEL = 'INFO'
    LOGGER_MODULE_LIST = ['blog', 'sqlalchemy.engine']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
