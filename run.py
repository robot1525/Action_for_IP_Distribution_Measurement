#coding=utf-8
 
from socket import *
import time

# 1. 创建udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
 
# 2. 准备接收方的地址
# '47.111.93.148'表示目的ip地址
# 22表示目的端口
dest_addr = ('47.111.93.148', 22)  # 注意 是元组，ip是字符串，端口是数字
 
# 3. 从本地读取数据
data_size = 32 * 2**20 ### 单位 B
send_data = "0" * data_size

# 4. 用udp套接字发送数据
packet_count = 0
now = 0
time_begin = time.time()
while True:
    udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
    packet_count += 1
    if (time.time() - time_begin) // 60 > now:
        print("Bandwidth: %.6f Mbps" % ((packet_count * len(send_data) * 8) / (time.time() - time_begin) / (2 ** 20)))
        now += 1

# 5. 关闭套接字
udp_socket.close()
