import struct

class ExchangeProtocol:
    def __init__(self, sock) -> None:
        self.socket = sock

    def send_msg(self, message: str):
        message = message.encode("gbk")
        header = struct.pack('!I', len(message))  # 获取长度 Header

        self.socket.sendall(header + message)

    def recv_msg(self):
        # 接收消息头
        header = self.socket.recv(4)

        if len(header) != 4:
            raise ValueError("Header 数据不完整. 无法解包.")

        message_len = struct.unpack('!I', header)[0]  # 解包消息长度

        # 接收消息内容
        data = self.socket.recv(message_len)

        return data.decode("gbk")