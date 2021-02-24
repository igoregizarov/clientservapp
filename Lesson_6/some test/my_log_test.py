import logging

import log

test_log = logging.getLogger('app')


def main():
    test_log.info('ERROR')


if __name__ == '__main__':
    main()
