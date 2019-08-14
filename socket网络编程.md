---
title: socket网络编程
---
# 服务器套接字
### 第一步:导入socket包
```
import sockt
```
### 第二步:创建套接字对象
socket(family, tyle)
family  - 设置IP类型， AF_INET(默认值) -> IP4 / AF_INET6 -> IP6
type - 设置传输类型  SOCK_STREAM(默认值) - TCP   SOCK_DGRAM - UDP
```
server = socket.socket()
```
### 第三步:绑定IP地址和端口
bind((IP地址, 端口号))
IP地址 - 服务器对应的计算机的IP地址，字符串
端口号 - 用来区分计算机上不同服务; 是一个数字，范围是0~65535;
但是其中1024以下的是著名端口，用来表示一个特殊的服务,一般不要用;
同一时间一个端口只能对应一个服务
```
server.bind(('10.7.187.149', 8081))
```
### 第四步:开始监听
listen(最大监听数) 
最大监听数 - 用来设置当前服务器一次可以处理多少个请求
```
server.listen(100)
print('开始监听')
```
### 第五步:让一个服务一直处于启动状态
```
while True:
	# 接收客户端发送的请求，返回建立的会话和客户端地址
	# 注意:这段代码会阻塞线程
	conversation, addr = server.accept()
	# 接收消息
	# recv(缓存大小)  - 获取客户端给服务器发送的数据，返回值是二进制
	re_data = conversation.recv(1024)
	print(re_data.decode('utf-8'))
	# 发送数据
	# send(数据) - 将制定的数据发送给客户端，数据要求是二进制的
	message = '你好！！！'
	conversation.send(message.encode(encoding='utf-8'))
	# 发送图片
    with open('lu.png', 'br') as f:
         content = f.read()
         conversation.send(content)
	# 关闭连接
	conversatio.close()
```
# 客户端套接字

### 第一步:导入socket包
```
import sockt
```
### 第二步:连接服务器
connect((服务器ip, 端口))
```
client.connect(('10.7.187.149', 8081))
```
### 第三步:发送消息
```
message = input('>>')
client.send(message.encode('utf-8'))
```
### 第四步: 接收消息
```
re_data = client.recv(1024)
print(re_data.decode('utf-8'))
```

```
# ========2.保持通话=============
while True:
    # 发送消息
    message = input('客户端:')
    client.send(message.encode('utf-8'))
    # 接收消息
    data = client.recv(1024)
    print('服务器:', data.decode('utf-8'))
    # ========1.接收图片==========
# 不断接收数据，直到接收完为止
# 创建一个空的二进制数据
data = bytes()
while True:
    re_data = client.recv(1024)
    data += re_data
    print('接收到数据!')
    if not re_data:
        break
print('数据接收完了')
with open('new.png', 'bw') as f:
    f.write(data)
```

# 网络请求
### 第一步:导入requests包
```
import requests
```
### 第二步:向服务器发送get请求
get(url, 参数字典) - 返回响应
```
# a.手动拼接url
url = 'https://www.apiopen.top/satinApi?type=1&page=1'
response = requests.get(url)
print(response)
# b.自动拼接url
url = 'https://www.apiopen.top/satinApi'
response = requests.get(url, {'type': 1, 'page': 1})
print(response)
```
### 第三步:获取响应头
```
header = response.headers
print(header)
```
### 第四步:获取响应体
```
# a.获取二进制格式的响应体
content = response.content
print(type(content))
# b.获取json格式响应体 - 自动将json数据转换成python
json = response.json()
print(type(json))
# c.获取字符串格式的响应体
text = response.text
print(type(text))
# 应用：下载网络图片
url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b10000_10000&sec=1543395098&di=2a5bbaa5600097b050ba69a688672de9&src=http://p0.qhimgs4.com/t0112e7ebfdef7f923d.jpg'
response = requests.get(url)
image_data = response.content
with open('王也.jpg', 'wb') as f:
    f.write(image_data
```

