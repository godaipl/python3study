# 使用系统函数fork()之后的web服务
import socket
import os
import time
import signal
import errno

SERVER_ADDRESS = (HOST, PORT) = '', 9998
REQUEST_QUEUE_SIZE = 2


def grim_reaper(signum, frame):
    # pid, status = os.wait()
    # print(
    #     'Child {pid} terminated with status {status}'
    #     '\n'.format(pid=pid, status=status)
    # )
    while True:
        try:
            pid, status = os.waitpid(
                -1,  # Wait for any child process
                os.WNOHANG  # Do not block and return EWOULDBLOCK error
            )
        except OSError:
            return

        if pid == 0:  # no more zombies
            return


def handle_request(client_connection):
    request = client_connection.recv(1024)
    print('Reciving request %s ' % request)

    http_response = """
            Hello, World!
            """
    print('Send response %s ...' % http_response)
    client_connection.sendall(http_response.encode())
    print('{pid} start to sleep \n'.format(pid=os.getpid()))
    time.sleep(60)
    print('{pid} sleep end \n'.format(pid=os.getpid()))


def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port} ...'.format(port=PORT))
    print('Parent PID (PID): {pid}\n'.format(pid=os.getpid()))

    signal.signal(signal.SIGCHLD, grim_reaper)

    while True:
        try:
            client_connection, client_address = listen_socket.accept()
        except IOError as e:
            code, msg = e.args
            # restart 'accept' if it was interrupted
            if code == errno.EINTR:
                continue
            else:
                raise

        pid = os.fork()
        if pid == 0:
            listen_socket.close()
            handle_request(client_connection)
            client_connection.close()
            os._exit(0)
        else:
            client_connection.close()


if __name__ == '__main__':
    serve_forever()
