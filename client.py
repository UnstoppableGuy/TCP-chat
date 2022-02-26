import socket
import threading
from globals import host,port
from colorama import Fore, init

init(autoreset=True)

nickname = input('Enter the nickname: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print('An error occured!')
            client.close()
            break


def write():
    while True:
        message = f'{nickname}: {input("")}'
        # message = Fore.BLUE + f'{nickname}:' + Fore.WHITE + f'{input("")}'
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
