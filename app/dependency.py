from __future__ import absolute_import

import configparser
import logging

config = configparser.ConfigParser()
config.read('error-config.ini')

fmt = config.get('logging_format', 'format', raw=True)


class LogFilter(logging.Filter):
    def __init__(self, log_file: str):
        self.log_file = log_file

    def filter(self, record):
        record.log_file = self.log_file
        return True


def setup_logger(logger_name, level=1):
    l = logging.getLogger(logger_name)

    def logForLevel(message, *args, **kwargs):
        l.log(level_num, message, *args, **kwargs)

    def logToRoot(message, *args, **kwargs):
        l.log(level_num, message, *args, **kwargs)

    for error_level in config['error_levels']:
        level_name = error_level
        level_num = int(config['error_levels'][error_level])

        method_name = level_name.lower()

        # Add Logging Level
        logging.addLevelName(level_num, level_name)
        setattr(logging, level_name, level_num)
        setattr(logging.getLoggerClass(), method_name, logForLevel)
        setattr(logging, method_name, logToRoot)

    # Add logging file name
    l.addFilter(LogFilter(log_file=logger_name))

    # Declare file and stream handlers
    fileHandler = logging.FileHandler(
        f'{logger_name}.log', mode='w')
    formatter = logging.Formatter(fmt)
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    # Set Level and Handlers
    l.setLevel(level)
    l.addHandler(fileHandler)
    l.addHandler(streamHandler)


setup_logger('log1')
setup_logger('log2')
setup_logger('log3')

log1 = logging.getLogger('log1')
log2 = logging.getLogger('log2')
log3 = logging.getLogger('log3')

log1.info('Info for log 1!')
log1.log(1, "Hello, World1!")
log2.info('Info for log 2!')
log2.log(2, "Hello, World2!")
log3.info('Info for log 3!')
log3.log(3, "Hello, World3!")
