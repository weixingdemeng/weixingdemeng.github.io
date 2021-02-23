# python项目部署
## centos部署django项目
- 安装ＭariaDB
安装命令
	yum -y install mariadb mariadb-server
安装完成后，首先启动ＭarIaDB
	systemctl start mariadb
设置开机启动
	systemctl enable mariadb
- 设置密码
命令
	mysql_secure_installation
	
	Enter current password for root:(初次运行直接回车)
	＃　设置密码
	Set root password? [Y/n] 是否设置root用户密码，输入y并回车或者直接回车
	New password: 设置root用户的密码
	Re-enter new password:再输入一次你设置的密码
	＃　其他配置
	Remove anonymout users? [Y/n]是否删除匿名用户，回车
	Disallow root login remotely? [Y/n]是否禁止root远程登录，回车
	Remove test database and access to it? [Y/n]是否删除test数据库，回车
	Reload pribilege tables now? [Y/n] 是否重新加载权限表，回车
	＃ 初始化MariaDB,接下来测试登录
	mysql -u root -p
- 开启远程连接
在mysql数据库中的user表中可以看到默认是只能本地连接的，所有可以添加一个新的用户，该用户可以远程访问
###### 创建用户
	# 先使用数据库
	use mysql;
	# 针对Ip
	create user 'root'@'192.168.10.10' identified by 'password';
	# 全部
	create user 'root'@'%' identified by 'password';
###### 授权
	# 给用户最大权限
	grant all pribileges on *.* to 'root'@'%' identified by 'password';
	# 给部分权限(test 数据库)
	grant all pribileges on test.* to 'root'@'%' indetified by 'password' with grant option;
	# 刷新权限表
	flush pribileges;
	# 查看
	show grants for 'root'@'localhost';
接下来就可以在远程的数据可视化工具中直接访问该服务器的mysql了。
	# 访问数据库
	mysql -u root -p
# 安装Python3.6
在centos中，系统默认只提供Python2.7的版本，但是项目我们使用的Python3.6的版本。
- 安装python3的方法
首先安装依赖包
	yum -y groupinstall "Development tools"
	yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqplite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
如果是安装3.7,还需要安装
	yum install libffi-devel -y
根据自己需求下载不同版本的Python3
	wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz
然后解压，进入该目录，安装Python3
	tar -xvJf Python-3.6.3.tar.xz
	cd python-3.6.2
	./configure --prifix=/usr/local/python3
	make && make install 
创建软链接
	ln -s /usr/local/python3/bin/python3 /usr/bin/python3
	ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
# 安装环境
- 安装virtualenv
	yum install python-virtualen-v
- 创建虚拟环境
	virtualenv --no-site-packages env
- 激活虚拟环境
	source bin/activate
- 安装环境需要的包
	pip install -r re_install.txt
	re_install.txt文件中记录的是需要安装包的名称以及对应的版本
# 部署
- 提示:Django的项目中，在工程目录下settings.py文件中有一个DEBUG=True参数，如果DEBUG=False则会出现js,css，img无法加载的情况出现。
- 原因：Django框架仅在开发模式下提供静态文件服务。当我开启DEBUG模式时，Django内置的服务器是提供静态文件的服务的，所以css等文件访问都没有问题，但是关闭DEBUG模式后，Django便不提供静态文件服务了。想一想这是符合Django的哲学的：这部分事情标准服务器都很擅长，就让服务器去做吧！
- 测试环境中部署方式
url.py中的修改：在测试环境中一般都直接使用python manage.py runserver的方式去运行项目。
	a) 修改settings.py配置文件中的DEBUG=False模式，修改ALLOEWD_HOST=['*']
    b) 修改工程目录下的urls.py
    from django.views.static import serve
    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^axf/', include('axf.urls', namespace='axf')),
        # 增加以下的url路由
    url(r'^static/(?P<path>.*)$', serve, {"document_root": 			settings.STATICFILES_DIRS[0]}),
	url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    url(r'^$', views.home)
]
- 中间件的修改
如果中间件是过滤那些地址不需要登录验证的话，就可以设置如下的static和media过滤地址的参数：
	# 验证用户的登录状态
	paths = ['/user/login/', '/user/register/',
         '/axf/market/', '/axf/marketparams/(\d+)/(\d+)/(\d+)/',
        '/static/[0-9a-zA-Z/\.]', '/media/[0-9a-zA-Z/\.]']
	for path in paths:
        if re.match(path, request.path):
            return None
# 正式环境中部署方式
- 正式环境中部署为nginx+uwsgi来部署django项目
- 安装nginx
添加nginx存储库
	yum install epel-release
- 安装nginx
	yum install nginx
- 运行nginx
Nginx不会自行启动，需要手动运行
	systemctl start nginx
- 查看nginx状态
	 systemctl status nginx 
- 启动/关闭/设置开机启动/禁止开机启动
	systemctl start/stop/enable/disable nginx
- 系统启动时启用Nginx
	systemstl enable nginx
- 如果你正在进行防火墙，请运行一下命令来允许HTTP和HTTPS通讯：
	sudo firewall-cmd --permanent --zone=public --add-service=http
	sudo firewall-cmd --permanent --zone=public ==add-service=https
	sudo firewall-cmd --reload
# 配置uwsgi
安装uwsgi
在虚拟环境中安装uwsgi,假设虚拟环境安装在/home/env/env中
	/home/env/env/bin/python3/pip3/ install uwsgi
# 配置项目代码，配置项目nginx,配置uwsgi.ini等
习惯每一个项目的配置文件，日志文件，虚拟环境放在一起，这方便开发，运维也方便维护
conf里面放配置文件,env里面为虚拟环境,logs为日志文件,src为项目文件
- 配置nginx.conf文件
首选：编写自己项目的nginx.conf文件如下，没一个项目对应有一个自己定义的nginx的配置文件
	server {
	listen             80;
	server_name ip localhost;
	access_log /home/logs/access.log;
	error_log /home/logs/error.log;
	location / {
	include uwsgi_params;
	uwsgi_pass 127.0.0.1:8800;
	}
	location /static/ {
	alias /home/src/acf/static/;
	expires 30d;
	}
	}
其次：修改总的nginx的配置文件，让总的nginx文件包含我们自定义的项目的conf文件，总的nginx配置文件在：/etc/nginx/nginx.conf中
	incluce /home/conf/*.conf;(这是我们自定义的Nginx的文件)
以上步骤完成后，重新nginx
	systemctl restart nginx
如果自定的conf文件没有错误的话，查看nginx的运行状态
- 配置uesgi文件
在conf文件夹下除了包含自定义的conf文件，还有我们定义的uwsgi.ini文件
	[uwsgi]
	projectname = project
	base = /home/src
	# 守护进程
	master = true
	# 进程个数
	processes = 4
	# 虚拟环境
	pythonhome = /home/env/project_env
	# 项目地址
	chdir = %(base)%(projectname)
	# 指定的python版本
	python_path = /usr/local/python3/bin/python3
	# 指定的uwsgi文件
	module = %(projectname).wsgi
	# 和nginx通信地址：端口
	socket = 127.0.0.1:8800
	# 日志文件地址
	logto = /home/logs/uwsgi.log
运行项目：
	/home/env/bin/python3/uwsgo --ini uwsgi.ini
	
	