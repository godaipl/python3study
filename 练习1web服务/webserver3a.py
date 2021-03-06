# 简单的webserver示范
import socket

SERVER_ADDRESS = (HOST, PORT) = '', 9998
REQUEST_QUEUE_SIZE = 2


def handle_request(client_connection):
    request = client_connection.recv(1024)
    print('Reciving request %s ' % request)

    http_response = """
            Hello, World!
            """
    print('Send response %s ...' % http_response)
    client_connection.sendall(http_response.encode())


def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(1)
    print('Serving HTTP on port %s ...' % PORT)

    while True:
        client_connection, client_address = listen_socket.accept()
        handle_request(client_connection)
        client_connection.close()

if __name__ == '__main__':
    serve_forever()