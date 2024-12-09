FROM golang:alpine as builder
LABEL maintainer="imkevinliao"
LABEL version="1.0.0"


WORKDIR /app

RUN apk add --no-cache git  && git clone --depth 1 https://github.com/XTLS/Xray-core.git . && \
    go mod download && \
    go build -o xray /app/main/

FROM python:3.10-alpine as runner


ENV UUID="8f0cd2a1-1da8-4d9d-9b94-eb82f899926c"
# 伪装的域名
ENV DOMAIN="addons.mozilla.org"
ENV PRIVATEKEY="YLXqVhX_JDjLHZ4kXsNqZzqiz9T-_FZ9SOkFL3JVGlc"
ENV PUBLICKEY="SG2EJoYrZB46Ug-WheG5bjuRy1yD85rISa3siK7gAjU"
# 服务器的ip地址
ENV HOST ""
# 服务器与容器的映射端口，7123:443
ENV SERVER_PORT 7123
ENV TZ=Asia/Shanghai
# 节点信息：
# vless://8f0cd2a1-1da8-4d9d-9b94-eb82f899926c@ip:7123?encryption=none&security=reality&type=tcp&sni=addons.mozilla.org&fp=chrome&pbk=SG2EJoYrZB46Ug-WheG5bjuRy1yD85rISa3siK7gAjU&flow=xtls-rprx-vision
WORKDIR /

COPY ./entrypoint.sh ./modfiy_config.py ./config_vision.json ./config_grpc.json /
COPY --from=builder /app/xray /

RUN apk add --no-cache curl && mkdir -p /var/log/xray && \
    chmod +x /entrypoint.sh /modfiy_config.py


ENTRYPOINT ["./entrypoint.sh"]

# 这个容器暴露的端口是协议配置的端口，如果修改需要一起修改
EXPOSE 443
