import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('localhost', 2501))

for i in range(100):
        message = f"Hi from Atlas {i}".encode('utf-8')
        sock.sendto(message, ('localhost', 2500))
        time.sleep(2)
