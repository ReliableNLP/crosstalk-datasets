import logging

def get_logger(LEVEL='info', log_file = None,name=None):
    head = '[%(asctime)-15s] [%(levelname)s] %(message)s'
    if LEVEL == 'info':
        logging.basicConfig(level=logging.INFO, format=head)
    elif LEVEL == 'debug':
        logging.basicConfig(level=logging.DEBUG, format=head)
    logger = logging.getLogger(name)
    if log_file != None:
        fh = logging.FileHandler(log_file)
        logger.addHandler(fh)
    return logger
