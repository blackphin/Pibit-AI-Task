from __future__ import absolute_import

import configparser
import logging

config = configparser.ConfigParser()
config.read('error-config.INI')

print(config['DEFAULT']['path'])     # -> "/path/name/"
config['DEFAULT']['path'] = '/var/shared/'    # update
config['DEFAULT']['default_message'] = 'Hey! help me!!'   # create

with open('FILE.INI', 'w') as configfile:    # save
    config.write(configfile)


levelName = "NEW"
levelNum = 15
methodName = levelName.lower()
fmt = '{"level": "%(levelname)s", "log_string": "%(message)s", "timestamp": "%(asctime)s", "metadata": {"source": "%(log_file)s"}}'


class AppFilter(logging.Filter):
    def __init__(self, log_file: str):
        self.log_file = log_file

    def filter(self, record):
        record.log_file = self.log_file
        return True


def setup_logger(logger_name, level=4):
    def logForLevel(message, *args, **kwargs):
        l.log(levelNum, message, *args, **kwargs)

    def logToRoot(message, *args, **kwargs):
        l.log(levelNum, message, *args, **kwargs)

    l = logging.getLogger(logger_name)

    logging.addLevelName(levelNum, levelName)
    setattr(logging, levelName, levelNum)
    setattr(logging.getLoggerClass(), methodName, logForLevel)
    setattr(logging, methodName, logToRoot)

    l.addFilter(AppFilter(log_file=logger_name))

    fileHandler = logging.FileHandler(
        fr'D:\OneDrive\Repositories\Pibit-AI-Task\{logger_name}.log', mode='w')
    formatter = logging.Formatter(fmt)
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)
    l.addHandler(streamHandler)

    # l = logging.LoggerAdapter(l, extra)


setup_logger('log1')
setup_logger('log2')
setup_logger('log3')

log1 = logging.getLogger('log1')
log2 = logging.getLogger('log2')
log3 = logging.getLogger('log3')

log1.info('Info for log 1!')
log2.info('Info for log 2!')
log1.error('Oh, no! Something went wrong!')
log3.log(15, "Hello, World!")
