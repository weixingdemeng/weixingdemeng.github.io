# docker
### 什么是docker
Docker是一个开源的应用容器引擎，它可以让开发者打包他们的应用以及依赖包到一个可移植的容器中，然后发布到任何流行的Linux机器上，也可以实现虚拟化。容器是完全使用沙箱机制，相互之间不会有任何接口。
### Docker作用
- 集装箱，可以把业务运行在任何地方
- 执行环境可移植，运维部署只需要提供注入了代码的docker容器即可。
- 用于不同项目的隔离出不同的开发环境，开发库等。
### docker的三个基本概念
- 镜像，它是docker运行容器的前提，可以看做是一个特殊的文件系统，除了提供容器运行时必须要的程序，库，资源，配置等文件外，还提供为运行时准备的一些配置参数（匿名卷，环境变量等）。镜像不包含任何动态数据，其内容在构建之后页不会被改变。
- 仓库，是存放镜像的场所
- 容器
### 要点
容器 = 镜像 + 读写层， 并且容器的定义并没有提及是否要运行容器。
### 运行态容器
一个运行态容器被定义为一个可读写的统一文件系统加上隔离的进程空间和包含其中的进程。
一个容器中的进程可能会对文件进行修改，删除，创建，这些改变都将作用与可读写层。
	docker run ubuntu touch my.txt
	find / -name my.txt(ubuntu容器不运行，也能够在主机的文件系统上找到这个新文件)
### docker命令
- docker create <image-id>为指定的镜像添加一个可读写层，构成一个新的容器。注意，这个容器并没有运行
- docker start  <container-id>为容器文件系统创建一个进程隔离空间。注意，每一个容器只能有一个进程隔离空间。
- docker run <image-id>先利用镜像创建一个容器，然后运行这个容器。
- git pull命令就是git fetch和git merge两个命令的组合，同样的docker run就是docker create和docker start两个命令的组合。
- docker ps列出所有运行总的容器。
- docker ps -a列出所有的容器。
- docker images列出所有顶层镜像。实际上，我们没有办法区分一个镜像和一个只读层，所以提供了top-level镜像，只有创建容器时使用的镜像或者是直接pull下来的镜像能被成为顶层镜像，并且每一个顶层镜像下面都隐藏了多个镜像层。
- docker images -a 列出所有的镜像，也可以说是列出所有的可读层。
- docker history 查看某一个image-id下的所有层
- docker stop <container-id>SIGTERM的信号，然后停止所有的进程。
- docker kill <container-id>向所有运行在容器中的进程发送了一个不友好的SIGKILL信号
- docker pause <container-id>
- docker rm <container-id>移除构成容器的可读写层。注意，这个命令只能对非运行容器执行。
- docker rmi <image-id>移除构成镜像的一个只读层，只能使用docker rmi来移除最顶层，可以使用－ｆ参数来强制删除中间的只读层。
- docker commit <container-id>将容易的可读写层转换为一个只读层，这样就把一个容器转换成了不可变的镜像。
- docker build反复执行多个命令
- docker exec <running-container-id>在运行中的容器执行一个新进程
- docker inspect <container-id> or <image-id>提取出容器或者镜像最顶层的元数据
- docker save <image-id>会创建一个镜像的压缩文件，这个文件能够在另外一个主机的Docker上使用。和export命令不同，这个命令为每一个层都保存了他们的元数据。这个命令只能对镜像生效。
- docker export <container-id>创建一个tar文件，并且移除了元数据和不必要的层，将多个层整合成了一个层，只保存了当前统一视角看到的内容（export后的容器再import到docker中，通过docker images -tree命令只能看到一个镜像，而save后的镜像则不同，它能够看到这个镜像的历史镜像）
