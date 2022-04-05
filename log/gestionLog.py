import logging

class Logger:
    def __init__(self, path):
        logging.basicConfig(
            filename=path,
            level=logging.DEBUG,
            format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
        )