# docker-compose
* 启动容器  
指定配置文件 docker-compose -f /path/to/docker-compose.yml up -d
```shell
docker-compose up -d 
```

# docker-compose 配置
```yaml
version: '3'

services:
  brook:
    image: txthinking/brook
    container_name: brook_server
    volumes:
      - ./brook.yaml:/brook.yaml
      - ./start_brook.sh:/start_brook.sh
    command: /bin/sh /start_brook.sh
    ports:
      - "9999:9999"
    restart: unless-stopped

  python:
    image: python:3.9-alpine
    container_name: python3.9
    volumes:
      - ./shared_data:/app/shared_data
      - ./brook.yaml:/app/brook.yaml
    working_dir: /app
    command: /bin/sh
    stdin_open: true
    tty: true
    environment:
      - PYTHONUNBUFFERED=1

volumes:
  shared_data:
```

# docker
```
docker pull txthinking/brook
docker run -d --name brook -p 9999:9999 txthinking/brook server -l :9999 -p password
docker exex -it brook sh
```
* 进入容器内部 docker ps -a 拿到 id， docker exec -it {id} sh  (进入容器开启一个shell会话）

# 示例
* xray : https://github.com/wulabing/xray_docker 打包构建
* 
