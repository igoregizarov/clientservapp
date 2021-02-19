import logging

logger = logging.getLogger('app')

format = logging.Formatter('%(levelname)-10s %(asctime)s %(message)s')

file_handler = logging.FileHandler('app.log', encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(format)

logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

if __name__ == '__main__':
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(format)
    logger.addHandler(console)
    logger.info('my logger')