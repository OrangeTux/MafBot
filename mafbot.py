#!/usr/bin/env python
import os
import sys
import logging

_curpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(_curpath)

formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

if __name__ == '__main__':
    from mafbot.actions import do_crime
    import time

    logger.debug('Starting mafbot')

    try:
        while True:
            do_crime()
            time.sleep(60)
    except Exception as e:
        print e

