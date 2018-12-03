'''
Created on Nov 6, 2015

@author: whu
'''
import logging

def get_logger(name):
    logger = logging.getLogger(name)
    logger.propagate = False
    formatter = logging.Formatter('[%(asctime)s: %(name)s/%(levelname)s] %(message)s')
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    return logger
#