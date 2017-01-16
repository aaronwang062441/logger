#!/usr/bin/env python
# encoding: utf-8

import logger

filep = "/tmp/mysql.log"
log = logger.Logger(filep)
log.debug("this is debug test")
log.debug("this is warning test")
