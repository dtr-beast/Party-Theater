import socket

HEADER = 64
PORT = 65432
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = "127.0.0.1"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((SERVER, PORT))

    def send(message):
        client.send(str.encode(message))
        print(client.recv(1024).decode(FORMAT))


    send("!p")
    input()
    send("!r")
    input()
    send("Hello Tim!")

    send(DISCONNECT_MESSAGE)
