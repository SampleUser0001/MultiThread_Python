# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os

import sys
from logutil import LogUtil

from sample.abstract import CookingUdon

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(PYTHON_APP_HOME + '/config/log_config.json')
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

class SingleThread(CookingUdon):
  def __init__(self):
    pass
  
  def run(self):
    logger.info('うどんを作ります。')
    self.boil_udon()
    self.make_tsuyu()
    logger.info('盛り付けます。')
    logger.info('うどんができました。')    
