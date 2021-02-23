# docker运用
### 安装docker 
在ubuntu系统中，安装docker 下载/更新curl
	sudo apt-get update $ sudo apt-get install curl
获取罪行的docker包
	curl -ssl https://get.docker.com/ | sh
### 制作镜像
运行交互式容器
	docker run (--name=容器名称) -it ubuntu /bin/bash
进入进行中的容器，安装相关Py库(pip install -r xxx.txt)
	docker exec -it 容器名或id /bin/bash
将安装好插件的容器编译好镜像并长传镜像
	docker commit -a 作者 -m 注释 容器名 镜像名：镜像版本号
	docker push 镜像名：镜像版本号
### 容器基本操作
查看运行中的容器
	docker ps
查看建立的容器
	docker ps -a/-l
停止守护式容器
	docker stop 容器id/容器名
	docker kill 容器id/容器名
重新启动停止的容器
	docker start 容器id/容器名
删除容器
	docker rm 容器id/容器名
删除镜像
	docker rmi 镜像id/镜像名
### docker学习网站
<http://www.docker.org.cn/>