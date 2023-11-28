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
