import logging
import os
import sys

try:
    import colorlog
except ImportError:
    pass


def setup_logging(log_file='books_log.log', log_level='INFO'):
    root = logging.getLogger()
    root.setLevel(log_level)
    format = '[%(asctime)s - %(name)s - %(levelname)s] - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    if 'colorlog' in sys.modules and os.isatty(2):
        cformat = '%(log_color)s' + format
        f = colorlog.ColoredFormatter(cformat, date_format,
                                      log_colors={'DEBUG': 'reset', 'INFO': 'green',
                                                  'WARNING': 'bold_yellow', 'ERROR': 'bold_red',
                                                  'CRITICAL': 'bold_red'})
    else:
        f = logging.Formatter('[%(asctime)s - %(name)s - %(levelname)s] - %(message)s')
    ch = logging.StreamHandler()
    ch.setFormatter(f)
    root.addHandler(ch)
    forfile = logging.Formatter('[%(asctime)s - %(name)s - %(levelname)s] - %(message)s')
    filelog_handler = logging.handlers.TimedRotatingFileHandler(filename=log_file, when='D', backupCount=7)
    filelog_handler.setFormatter(forfile)
    root.addHandler(filelog_handler)

# setup_logging()
# log = logging.getLogger(__name__)
