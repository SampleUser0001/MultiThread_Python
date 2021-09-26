# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os

import sys
from logutil import LogUtil
import time

from abc import ABCMeta, abstractmethod

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(PYTHON_APP_HOME + '/config/log_config.json')
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

class CookingUdon(metaclass=ABCMeta):
  @abstractmethod
  def run():
    pass
  
  @staticmethod
  def boil_udon():
    logger.info('  うどんを茹でます')
    time.sleep(3)
    logger.info('  うどんが茹で上がりました。')
  
  @staticmethod
  def make_tsuyu():
    print('  つゆを作ります。')
    time.sleep(2)
    print('  つゆができました。')
