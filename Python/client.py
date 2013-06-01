import socket
import sys

HOST, PORT = "localhost", 9999
print("Decalage piece ?")
decalage = input()
print("Angle piece ?")
angle = input()

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(decalage + "\n", "utf-8"))
    sock.sendall(bytes(angle + "\n", "utf-8"))

finally:
    sock.close()

print("Decalage envoyé :     {}".format(decalage))
print("Angle envoyé : {}".format(angle))
