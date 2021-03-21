import subprocess

process = []

while True:
    action = input('Выберите действие: q - выход , s - запустить сервер и клиенты, x - закрыть все окна:')

    if action == 'q':
        break
    elif action == 's':
        # process.append(subprocess.Popen('python server.py', creationflags=subprocess.CREATE_NEW_CONSOLE))
        # n = int(input('Сколько создать клинтов отправляющих сообщения? - '))
        # for i in range(n - 1):
        #     process.append(subprocess.Popen('python client.py send', creationflags=subprocess.CREATE_NEW_CONSOLE))
        # n = int(input('Сколько создать клинтов принимающих сообщения? - '))
        # for i in range(n - 1):
        #     process.append(subprocess.Popen('python client.py read', creationflags=subprocess.CREATE_NEW_CONSOLE))
        process.append(subprocess.Popen('python server.py', creationflags=subprocess.CREATE_NEW_CONSOLE))
        process.append(subprocess.Popen('python client.py send', creationflags=subprocess.CREATE_NEW_CONSOLE))
        process.append(subprocess.Popen('python client.py read', creationflags=subprocess.CREATE_NEW_CONSOLE))
    elif action == 'x':
        while process:
            victim = process.pop()
            victim.kill()