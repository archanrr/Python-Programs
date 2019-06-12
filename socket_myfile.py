import socket


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 80

ip = socket.gethostbyname("google.com")
print(ip)
client.connect(ip)