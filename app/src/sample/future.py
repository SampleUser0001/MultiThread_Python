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

class UseFuture(CookingUdon):
  kinds = ['たぬき', 'かけ', 'ざる', 'きつね', '天ぷら', '肉']

  def __init__(self):
    self.executor = ThreadPoolExecutor(max_workers=2)
    self.futures = []

  def make_udon(self, kind):
    udon = '{}うどん'.format(kind)
    logger.info('  {}を作ります。'.format(udon))
    time.sleep(3)
    return udon
    
  def run(self):
    for kind in UseFuture.kinds:
      logger.info('{}うどん オーダーはいりました。'.format(kind))
      future = self.executor.submit(self.make_udon, kind)
      self.futures.append(future)

    for future in self.futures:
      logger.info('{}お待たせしました。'.format(future.result()))
    
    self.executor.shutdown()