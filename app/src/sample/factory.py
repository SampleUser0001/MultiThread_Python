# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os

import sys
from logutil import LogUtil
from enum import Enum

from sample.single_thread import SingleThread
from sample.multi_thread_1 import MultiThread01
from sample.thread_pool_executor import UseThreadPoolExecutor
from sample.future import UseFuture

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(PYTHON_APP_HOME + '/config/log_config.json')
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

class UdonCookerFactory(Enum):
  SINGLE_THREAD = (
    "single_thread", SingleThread())
  MULTI_THREAD_01 = (
    "multi_thread_1", MultiThread01())
  USE_THREAD_POOL_EXECUTOR = (
    "thread_pool_executor", UseThreadPoolExecutor())
  USE_FUTURE = (
    "future", UseFuture())

  def __init__(self, id, instance):
    self.id = id
    self.instance = instance

  @staticmethod
  def create(instance_name):
    for em in UdonCookerFactory:
      if em.id == instance_name:
        return em.instance
    raise ValueError("{} is not found.".format(instance_name))