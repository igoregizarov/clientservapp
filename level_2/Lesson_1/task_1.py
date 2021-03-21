"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping
будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел
должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять
их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес
сетевого узла должен создаваться с помощью функции ip_address().
"""

from ipaddress import ip_address
from subprocess import Popen, PIPE


def host_ping(list_ip_adress, timeout=500, requests=1):
    results = {'Доступные узлы': '', 'Недоступные узлы': ''}
    for address in list_ip_adress:
        try:
            address = ip_address(address)
        except Exception:
            pass
        proc = Popen(f"ping {address} -w {timeout} -n {requests}", shell=False, stdout=PIPE)
        proc.wait()
        if proc.returncode == 0:
            results['Доступные узлы'] += f"{str(address)}\n"
            res_string = f'{address} - Узел доступен'
        else:
            results['Недоступные узлы'] += f"{str(address)}\n"
            res_string = f'{address} - Узел не доступен'
        print(res_string)
    return results


def ip_address():
    lst = []
    while True:
        addr = input('Введите адресс в фомате 8.8.8.8 или yandex.ru через запятую.\nДля выхода - q:\n')
        if addr != 'q':
            l = addr.split(',')
            lst += l
            print(lst)
        else:
            break
    return lst


if __name__ == '__main__':
    host_ping(ip_address())
