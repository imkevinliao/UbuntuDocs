#!/bin/sh

# 执行 Python 脚本来修改配置
python3 /modfiy_config.py

exec /xray -config /config.json
