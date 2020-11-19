"""
Author:     LanHao
Date:       2020/11/16
Python:     python3.6

"""
import time
import logging
from logging import Handler
from logging.handlers import HTTPHandler,QueueHandler





logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


host = '127.0.0.1:8080'
url = '/logs/apis'
handler = HTTPHandler(host, url, method='POST')
logger.addHandler(handler)
for i in range(2):
    logger.critical("你好")

# time.sleep(10)