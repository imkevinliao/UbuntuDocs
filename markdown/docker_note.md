# 常见命令
* 列出所有的容器
```shell
docker ps -a
```
* 停止所有容器
```shell
docker kill $(docker ps -a -q)
```
```shell
docker stop $(docker ps -a -q)
```
* 删除所有容器
```shell
docker rm $(docker ps -a -q)
```

* 删除所有镜像
```shell
docker rmi $(docker images -q)
```

* 停止docker服务
```shell
systemctl stop docker.socket && systemctl stop docker.service && systemctl stop docker
```

# 说明
* 控制容器运行: docker start/stop/restart + id

# docker 笔记
- <https://mp.weixin.qq.com/s/fd-_oY624s0sh25Dkf6iGA> 常见操作

```
# filebrowser
# mkdir /root/filebrowser_data/
# touch
#docker run \
#    -v /path/to/root:/srv \
#    -v /path/to/filebrowser.db:/database/filebrowser.db \
#    -v /path/to/settings.json:/config/settings.json \
#    -e PUID=$(id -u) \
#    -e PGID=$(id -g) \
#    -p 8080:80 \
#    filebrowser/filebrowser:s6
```

# docker 快速上手
-q 列出容器 id 而不是容器的所有信息
```
停止所有 docker 容器
docker kill $(docker ps -a -q)
docker stop $(docker ps -a -q)
删除所有容器
docker rm $(docker ps -a -q)
删除所有镜像
docker rmi $(docker images -q)
停止docker服务
systemctl stop docker
无法停止：
Warning: Stopping docker.service, but it can still be activated by: docker.socket
systemctl stop docker.socket
systemctl stop docker.service
```
基本操作
```
列出所有容器 第一行即 id
docker ps -a
docker start stop restart + id
```

