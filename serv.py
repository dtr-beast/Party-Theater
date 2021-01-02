import socket
import threading

HEADER = 64
PORT = 65432
SERVER = '127.0.0.1'
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))


def handle_client(conn, address):
    print(f"[NEW CONNECTION] {address[0]}:{address[1]} connected.\n")

    connected = True
    while connected:
        data = conn.recv(1024).decode()

        # Disconnect Message
        if data == DISCONNECT_MESSAGE:
            connected = False
        else:
            # Pause
            if data == '!p':
                print(f'Pause request from {address[0]}:{address[1]}')
                conn.send(str.encode(f'!p'))
            # Resume
            elif data == '!r':
                print(f'Resume request from {address[0]}:{address[1]}')
                conn.send(str.encode(f'!r'))
            else:
                conn.send(str.encode('Got yo message!'))

            print(f"[{address}] {data}")
        # conn.send(f'.'.encode(FORMAT))

    conn.close()


def start():
    server.listen(10)
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()
