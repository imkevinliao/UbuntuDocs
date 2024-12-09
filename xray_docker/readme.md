# 前言
这个 Dockerfile 并不完美，但是可用，没有规划设计导致体验上存在问题

参考了两位大佬的设计：
1. https://github.com/wulabing/xray_docker
2. https://github.com/mack-a/v2ray-agent

# 一键部署
注意：这个是需要使用 Dockerfile 自行构建镜像，而不是直接 docker pull 拉取。

```
docker build -t xray . && docker run -d --name xray --restart=always -p 7333:443 -e SERVER_PORT=7123 xray && docker exec -it  xray cat /config_info.txt
```

# 开发时候使用的命令

```
docker build -t xray . && docker run -d --name xray --restart=always -p 7333:443 -e SERVER_PORT=7123 xray
```

```
docker exec -it xray
```

```
docker stop xray && docker rm xray && docker rmi xray
```

```
docker logs -f xray
```
# 总结
Docker 确实是一个对于个人开发者很好用的工具，解决了开发的环境问题
