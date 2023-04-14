import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('localhost', 2500))

while True:
        response, peer_address = sock.recvfrom(1024)
        print(response.decode('utf-8'), peer_address)
