import socket

HOST, PORT = '', 9998

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

sock.sendall(b'Test')
response = sock.recv(1024)

print('Receving response %s ' % response.decode())