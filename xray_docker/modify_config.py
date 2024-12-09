import ipaddress
import json
import os
import re
import shutil
import subprocess
import random

xray_path = "/xray"


class Params:
    uuid = ""
    domain = ""
    private_key = ""
    public_key = ""
    host = ""
    port = ""


def is_valid_ip(check_string):
    try:
        ipaddress.ip_address(check_string)
        return True
    except ValueError:
        return False


def get_ip():
    ip = ""
    commands = ["curl --ipv4 api.ipify.org", "curl --ipv4 ifconfig.me", "curl --ipv4 ip.me", "curl --ipv4 ipinfo.io/ip"]
    for command in commands:
        result = subprocess.run(command.split(" "), capture_output=True, text=True)
        output = result.stdout.strip()
        if is_valid_ip(output):
            ip = output
            break
    if not ip:
        raise Exception("Not Get Public IP")
    return ip


def get_domain():
    fake_domains = [
        "addons.mozilla.org",
        "www.amd.com",
        "www.samsung.com",
        "www.swift.com",
        "www.cisco.com",
        "www.apple.com"
    ]
    return random.choice(fake_domains)


def get_uuid():
    output = subprocess.getoutput(f"{xray_path} uuid").strip()
    return output


def get_key():
    output = subprocess.getoutput(f"{xray_path} x25519")
    private_key = re.search(r"Private key:\s*(\S+)", output).group(1).strip()
    public_key = re.search(r"Public key:\s*(\S+)", output).group(1).strip()
    return private_key, public_key


def prepare():
    uuid = os.getenv("UUID", "")
    domain = os.getenv("DOMAIN", "")
    private_key = os.getenv("PRIVATEKEY", "")
    public_key = os.getenv("PUBLICKEY", "")
    host = os.getenv("HOST", "")
    port = os.getenv("SERVER_PORT", "")
    if not port:
        port = "443"
    if not uuid:
        uuid = get_uuid()
    if not domain:
        domain = get_domain()
    if not private_key or not public_key:
        private_key, public_key = get_key()
    if not host:
        host = get_ip()
    param = Params()
    param.uuid = uuid
    param.domain = domain
    param.private_key = private_key
    param.public_key = public_key
    param.host = host
    param.port = port
    return param


def core():
    param = prepare()
    filepath_vision = os.path.join("/config_vision.json")
    filepath_grpc = os.path.join("/config_grpc.json")
    for filepath in [filepath_vision, filepath_grpc]:
        with open(filepath, 'r', encoding='utf8') as f:
            content_dict = json.load(f)
        # content_dict["inbounds"][0]["port"] = 443 这个和EXPOSE 443相关
        content_dict["inbounds"][0]["settings"]["clients"][0]["id"] = param.uuid
        content_dict["inbounds"][0]["streamSettings"]["realitySettings"]["dest"] = f"{param.domain}:443"
        content_dict["inbounds"][0]["streamSettings"]["realitySettings"]["serverNames"] = [param.domain]
        content_dict["inbounds"][0]["streamSettings"]["realitySettings"]["privateKey"] = param.private_key
        content_dict["inbounds"][0]["streamSettings"]["realitySettings"]["publicKey"] = param.public_key
        with open(filepath, 'w', encoding='utf8') as f:
                json.dump(content_dict, f, indent=4, ensure_ascii=False)
    shutil.copyfile(filepath_vision, "/config.json")
    vision = f"vless://{param.uuid}@{param.host}:{param.port}?encryption=none&security=reality&type=tcp&sni={param.domain}&fp=chrome&pbk={param.public_key}&flow=xtls-rprx-vision"
    node = vision
    # grpc = f"vless://{param.uuid}@{param.host}:{param.port}?encryption=none&security=reality&type=grpc&sni={param.domain}&fp=chrome&pbk={param.public_key}&path=grpc&serviceName=grpc"
    # node = grpc
    with open("/config_info.txt", "w", encoding='utf8') as f:
        f.write(node + "\n")


if __name__ == '__main__':
    core()
