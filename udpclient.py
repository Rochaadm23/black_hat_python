import socket


target_host = '127.0.0.1'
target_port = 80

# Criar um objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# envuia alguns dados
client.sendto(b'AAABBBCCC', (target_host, target_port))

# recebe alguns dados
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()
