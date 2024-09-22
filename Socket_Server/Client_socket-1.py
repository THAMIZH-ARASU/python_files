import socket

host_ip="127.0.0.1"
server_port=9999

data="Allow me for 10mins\n"

tcp_client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    tcp_client.connect((host_ip,server_port))
    tcp_client.sendall(data.encode())



    received=tcp_client.recv(1024)

finally:
    tcp_client.close()


print("Bytes Sent:  {}".format(data))
print("Bytes Received:  {}".format(received.decode()))
