# git 配置
```
git config --global alias.gp pull
git config --global alias.co checkout
git config --global alias.st status
git config --global alias.br branch
git config --global alias.ci commit

个人偏好： git config --global alias.lg "log --no-merges --color --graph --date=format:'%Y-%m-%d %H:%M:%S' --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Cblue %s %Cgreen(%cd) %C(bold blue)<%an>%Creset' --abbrev-commit"

更加详细： git config --global alias.lg "log --no-merges --color --stat --graph --date=format:'%Y-%m-%d %H:%M:%S' --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Cblue %s %Cgreen(%cd) %C(bold blue)<%an>%Creset' --abbrev-commit"

网上通常： git config --global alias.lg --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cd) %C(bold blue)<%an>%Creset' --abbrev-commit --
```
git 一键配置

```
git config --global alias.gp pull && git config --global alias.co checkout && git config --global alias.st status && git config --global alias.br branch && git config --global alias.ci commit && git config --global alias.lg "log --no-merges --color --graph --date=format:'%Y-%m-%d %H:%M:%S' --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Cblue %s %Cgreen(%cd) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

# git 服务器搭建
1. 先切换 root 用户
2. 安装 git：apt install git
3. 创建 git 用户：adduser git
4. 切换为 git 用户，并进入 git 用户目录：su git, cd ~
5. 创建一个裸仓库：git init --bare sample.git
6. 准备认证环境：mkdir .ssh, touch .ssh/authorized_keys, chmod 600 ./ssh/authorized_keys
7. 退出 git 用户：exit
8. 此时我们回到了 root 用户，禁用 shell 登录，先查看 git-shell 路径：`which git-shell, vim /etc/passwd`
   找到 `git:x:1001:1001:,,,:/home/git:/bin/bash` , 更改为 `/home/git:/usr/bin/git-shell`, 注意 /usr/bin/git-shell 是 which git-shell 显示的路径，根据实际情况修改
9. 收集需要登录用户的公钥，拷贝到 /home/git/.ssh/authorized_keys
10. 验证登录：git clone git@ip:/home/git/sample.git （出现裸仓库警告证明 clone 成功： warning: You appear to have cloned an empty repository.）

# 注意事项
一定要禁止 git 用户使用 shell 登陆，安全问题并非小事

如果创建 git 用户后，立即修改 /etc/passwd，会导致后续无法切换到 git，在 su git 会报错，
当然后续直接使用 root 进行后面的操作也是没有问题的，只是必须要记得把后面操作的所有文件的权限都改为 git，
否则会出现权限相关的问题，所以建议操作完成后再禁止 shell 登录。

# git 注意
为项目单独配置用户名和邮箱
```
git config user.name imkevin && git config user.email imkevin
```
为所有项目配置用户名和邮箱
```
git config --global user.name imkevin && git config --global user.email imkevin
```

