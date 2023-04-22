from SocketProtocol import ExchangeProtocol

import socket

# 定义服务器 IP 和端口号
ip, port = '127.0.0.1', 8888

# 创建 socket 客户端并连接服务器
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))

ep = ExchangeProtocol(client)
while 1:
    ep.send_msg(input(":"))

# 关闭 socket 连接
client.close()
