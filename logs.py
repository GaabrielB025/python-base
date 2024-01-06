#!/usr/bin/env python3

import logging
from logging import handlers
import os

# TODO: Função
log_level = os.getenv('LOG_LEVEL', 'WARNING').upper()

logger = logging.Logger(log_level)
fh = handlers.RotatingFileHandler('my_log.log', maxBytes=1000, backupCount=5)
fh.setLevel(log_level)
# ch = logging.StreamHandler()
# ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
# ch.setFormatter(fmt)
fh.setFormatter(fmt)
logger.addHandler(fh)

logger.debug('Mensagem de DEBUG')
logger.info('Mensagem de INFO')
logger.warning('Mensagem de WARNING')
logger.error('Mensagem de ERRO')
logger.critical('Mensagem de CRITICAL')

try:
    1 / 0
except ZeroDivisionError as e:
    logging.warning("%s", str(e))

