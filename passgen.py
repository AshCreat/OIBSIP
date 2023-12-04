import socket

HEADER = 1024
PORT = 1234

def connect_to_server(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to server")

    return client_socket

def send_message(client_socket, message):
    msg_header = f"{len(message):<{HEADER}}".encode('utf-8')
    client_socket.sendall(msg_header + message.encode('utf-8'))

if __name__ == "__main__":
    host = 'localhost'
    port = PORT

    client_socket = connect_to_server(host, port)

    while True:
        message = input("Enter message: ")
        send_message(client_socket, message)


