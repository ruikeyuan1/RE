import socket

while True:
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("127.0.0.1", 1236))
        data = input()
        print('send to server: ' + data)
        client_socket.send(data.encode())
        print(client_socket.recv(2048).decode())
        client_socket.close()
    except Exception as msg:
        print(msg)
