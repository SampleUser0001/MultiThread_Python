# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os

import sys
from logutil import LogUtil

import time
from concurrent.futures import ThreadPoolExecutor

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

class UseThreadPoolExecutor(CookingUdon):
  def __init__(self):
    pass
  
  def run(self):
    # 何食うどん作るか
    meal_count = 100
    
    # Thread Pool生成する。
    tpe = ThreadPoolExecutor(max_workers=10)

    logger.info('うどんを{}食茹でます。'.format(meal_count))
    
    for _ in range(meal_count):
      tpe.submit(self.boil_udon)
    
    tpe.shutdown()
    logger.info('うどんを{}食茹でました。'.format(meal_count))
