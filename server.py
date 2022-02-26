from socket import socket
import threading
import socket
from colorama import Fore, init
from globals import host,port

init(autoreset=True)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


def broadcast(message):
    mesg = message.decode('ascii')
    # print(type(mesg),mesg)
    if mesg.split(' ')[1] in nicknames:
        try:
            index = nicknames.index(mesg.split(' ')[1])
            current_client = clients[index]
            current_client.send(message)
        except TypeError:
            print('problem')
    else:
        for client in clients:
            client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send(f'NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(Fore.GREEN + f'Nickname of the client is {nickname}!')
        broadcast(f'Server message: {nickname} joined the chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii)'))
        print(f'{nicknames} on server now')
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print(Fore.YELLOW + 'Server is listening')
receive()
