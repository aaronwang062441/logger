#!/usr/bin/env python
# encoding: utf-8

import logging

class Logger(object):
    """
    Class of simple log functions
    """
    def __init__(self, lfile):
        logger = logging.getLogger("mlog")
        logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(lfile)
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s", "%a, %d %b %Y %H:%M:%S")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        self.__logger = logger

    def debug(self, msg):
        """
        Log a message with level DEBUG on the logger
        """
        self.__logger.debug(msg)

    def warning(self, msg):
        """
        Log a message with level WARNING on the logger
        """
        self.__logger.warning(msg)

