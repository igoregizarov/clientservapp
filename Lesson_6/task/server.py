from socket import AF_INET, socket, SOCK_STREAM
import time
import json

import logging

import my_log_test

test_log = logging.getLogger('app')


class Log():
    def __init__(self):
        pass

    def __call__(self, func):
        def decorated(*args, **kwargs):
            debug_log = open("server_func.log", "a", encoding='utf-8')
            debug_log.write(f"{time.ctime()} Вызов {func.__name__}: {args}, {kwargs}\n")
            res = func(*args, **kwargs)
            debug_log.write(f"{func.__name__} вернула {res}\n")
            return res

        return decorated


@Log()
def connect_done():
    test_log.info('Server Connect is Done!')


@Log()
def send_msg_to_client(var):
    if var == 'presence':
        msg = {
            "response": 200,
            "alert": "Connect is done!",
            "time": time.ctime()
        }
    else:
        msg = {
            "response": 400,
            "alert": "Something wrong!",
            "time": time.ctime()
        }
    return msg


if __name__ == '__main__':
    from common.configs import *

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', PORT))
    s.listen(LISTEN)

    while True:
        client, addr = s.accept()
        connect_done()
        data = client.recv(4096)
        data = data.decode('utf-8')
        data = json.loads(data)
        msg = send_msg_to_client(data['action'])
        msg = json.dumps(msg)
        client.send(msg.encode('utf-8'))
        client.close()
