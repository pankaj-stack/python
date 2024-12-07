import logging

logger = logging.getLogger('studentlogger')
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler('student.log', mode='w')
fileHandler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

logger.critical('critical message from student module')
logger.error('error message from student module')
logger.warning('warning message student test module')
logger.info('info message by student module')
logger.debug('debug message by student module')
