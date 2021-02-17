import logging

import log

test_log = logging.getLogger('app' + __name__)


def main():
    test_log.info('Info')


if __name__ == '__main__':
    main()
