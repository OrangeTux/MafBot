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
    logger.debug('Starting mafbot')

    do_crime()
