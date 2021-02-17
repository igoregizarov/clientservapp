from socket import AF_INET, socket, SOCK_STREAM
import json
from sys import argv, exit
import time

import logging

import my_log_test

test_log = logging.getLogger('app')


def log(func):
    def wrapper(*args, **kwargs):
        debug_log = open("client_func.log", "a", encoding='utf-8')
        debug_log.write(f"{time.ctime()} Вызов {func.__name__}: {args}, {kwargs}\n")
        res = func(*args, **kwargs)
        debug_log.write(f"{func.__name__} вернула {res}\n")
        return res

    return wrapper


@log
def connect_done():
    test_log.info('Client Connect is Done!')


@log
def connect_answer():
    test_log.info('Correct answer!')


@log
def make_presence_msg():
    msg = {
        "action": "presence",
        "time": time.ctime()
    }
    return msg


if __name__ == '__main__':
    with open("common/settings.json") as f:
        data = json.load(f)

    name_script, host, = argv
    if host != '127.0.0.1':
        print('Error host')
        exit()

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((host, data['port']))
    connect_done()

    msg = make_presence_msg()
    msg = json.dumps(msg)

    s.send(msg.encode('utf-8'))
    data = s.recv(4096)
    data = data.decode('utf-8')
    data = json.loads(data)
    print(data["alert"])
    connect_answer()
    s.close()
