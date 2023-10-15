import socket
UDP_IP = "144.32.210.197"
UDP_PORT = 16759
MESSAGE = "BANK-PRESS 96 11"
print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))