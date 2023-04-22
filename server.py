import socket
from SocketProtocol import ExchangeProtocol

# 定义 IP 和端口号
ip, port = '127.0.0.1', 8888

# 创建 socket 服务器
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(1)

# 等待客户端连接
print('Waiting for client connection...')
client_sock, client_addr = server.accept()

ep = ExchangeProtocol(client_sock)
while 1:
    print(ep.recv_msg())

# 关闭 socket 连接
client_sock.close()
server.close()
