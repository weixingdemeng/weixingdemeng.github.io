# 克隆github项目

- 1 、新建文件夹，右键选择git bush here
- 2、git init 初始化仓库
- 3、下发命令

```git
git config --global user.name "your Account" 
git config --global user.email "your emai" 
```
- 4、生成ssh公钥
```git
ssh-keygen -t rsa -C “you email" 
```
- 5、打开文件~/.ssh文件
- 6、将.pub文件内容放在github->settings中Add SSH Key
- 7、git clone url
- 8、打开工程

