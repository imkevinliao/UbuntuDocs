# 脚本
- https://github.com/Jrohy/multi-v2ray （自定义）
- https://github.com/mack-a/v2ray-agent （推荐）
- https://github.com/wulabing/V2Ray_ws-tls_bash_onekey
- https://github.com/233boy/v2ray/tree/master （推荐：适合新手小白 ）
- https://github.com/wulabing/Xray_onekey
******
- https://github.com/emptysuns/Hi_Hysteria
- https://github.com/yonggekkk/Hysteria-yg
- https://github.com/yonggekkk/sing-box_hysteria2_tuic_argo_reality

# 新建服务器
在创建 VPS 服务器前添加额外脚本：
```
sudo useradd kevin -m -s /bin/bash
echo 'kevin:123456' | sudo chpasswd
sudo sed -i '52c PasswordAuthentication yes' /etc/ssh/sshd_config
sudo service sshd restart
sudo sed -i '20a kevin    ALL=(ALL:ALL) NOPASSWD:ALL' /etc/sudoers
```
直接开启root用户登录
```
echo root:kevinstarry |sudo chpasswd root
sudo sed -i 's/^.*PermitRootLogin.*/PermitRootLogin yes/g' /etc/ssh/sshd_config;
sudo sed -i 's/^.*PasswordAuthentication.*/PasswordAuthentication yes/g' /etc/ssh/sshd_config;
sudo service sshd restart
```

公钥拷贝到服务器使用 ssh 登录远程服务器(ip替换为实际ip)：
```
ssh-copy-id -i ~/.ssh/id_rsa.pub kevin@ip
ssh kevin@ip
```

---
这里可以先一边更新：`sudo apt update -y && sudo apt upgrade -y`

---

使用 kevin 登录服务器后切换 root 用户(使用ssh-keygen是为了方便直接生成./ssh文件夹）
```
ssh-keygen

cp /home/kevin/.ssh/authorized_keys /root/.ssh/authorized_keys
```
然后编辑 ssh 配置文件：
```
vim /etc/ssh/sshd_config
```

登录服务器后，开启禁止root用户密码登录：PermitRootLogin prohibit-password

禁止密码登录（确保root ssh正常连接后再改这个）：PasswordAuthentication no

禁止空密码登录：PermitEmptyPasswords no

重启 sshd 服务 `systemctl restart sshd`

使用 ssh 登录：`ssh root@ip`，登陆后删除 kevin（注意需要先退出kevin，否则由于被使用，无法删除）`userdel -r kevin`

此时 Linux 环境准备完毕！
# 搭建梯子以及其他
## V2ray
```
自选一个脚本
source <(curl -sL https://multi.netlify.app/v2ray.sh) --zh

1. 更改传输方式 vless + tcp
2. 更改 TLS
3. 更改端口为 443

开启 BBR 加速
wget --no-check-certificate -O tcp.sh https://raw.githubusercontent.com/Mufeiss/Linux-NetSpeed/master/tcp.sh && chmod +x tcp.sh && ./tcp.sh

wget -N --no-check-certificate "http://cdn.1doc.top/sh/tcp.sh" && chmod +x tcp.sh && ./tcp.sh
```
## Vnstat
```
apt install vnstat
vim /root/auto-shutdown.sh

#!/bin/bash
TRAFF_TOTAL=900 #流量额度，单位 GB。
TRAFF_USED=$(vnstat --oneline b | awk -F';' '{print $11}')
CHANGE_TO_GB=$(expr $TRAFF_USED / 1073741824)

if [ $CHANGE_TO_GB -gt $TRAFF_TOTAL ]; then
    shutdown -h now
fi

crontab -e
*/10 * * * * /root/auto-shutdown.sh > /dev/null 2>&1

crontab log enable：
sudo vim /etc/rsyslog.d/50-default.conf
cron.* /var/log/cron.log （删除前面的注释）
sudo systemctl restart rsyslog.service
# 每三个月的 1 号删除定时任务日志
0 0 1 */3 * rm -f /var/log/cron.log
----------------------------------------------------
时区时间校准： timedatectl set-timezone Asia/Shanghai
24小时制度：localectl set-locale LC_TIME="en_US.UTF-8"
定时任务测试：https://crontab.guru/
vnstat 配置文件 /etc/vnstat.conf 默认每月 1 号开始统计
vnstat -d
vnstat -m
```
## FileBrowser
```
1. AWS LightSail 服务器开放端口：50000
2. curl -fsSL https://raw.githubusercontent.com/filebrowser/get/master/get.sh | bash
3. filebrowser -d /etc/filebrowser.db config init && filebrowser -d /etc/filebrowser.db config set --address 0.0.0.0 && filebrowser -d /etc/filebrowser.db config set --port 50000
4. sudo vim /etc/systemd/system/filebrowser.service

[Unit]
Description=File browser
After=network.target

[Service]
ExecStart=/usr/local/bin/filebrowser -d /etc/filebrowser.db

[Install]
WantedBy=multi-user.target

5. sudo filebrowser users add admin 123456 --perm.admin -d /etc/filebrowser.db && sudo filebrowser users update admin --password 123456 --perm.admin -d /etc/filebrowser.db && sudo systemctl enable filebrowser.service

6.
# 配置 SSL （一旦配置 SSL 后，FileBrowser 将只支持 HTTPS，不支持 HTTP。
# 证书根据实际选择（实际证书路径替换）
域名：{你的域名}
filebrowser -d /etc/filebrowser.db config set --cert /root/.acme.sh/{你的域名}_ecc/{你的域名}.cer --key /root/.acme.sh/{你的域名}_ecc/{你的域名}.key
取消证书（如果 FileBrowser 在运行需要先关闭）：filebrowser -d /etc/filebrowser.db config set --cert "" --key ""

7.访问测试：
https://{你的域名}:50000

没配置域名的话：http://{你的ip}:50000
----------------------------------------------
sudo systemctl start filebrowser.service
sudo systemctl stop filebrowser.service
sudo systemctl status filebrowser.service
```
## 解锁流媒体
- <https://github.com/yonggekkk/warp-yg> `wget https://gitlab.com/rwkgyg/CFwarp/raw/main/CFwarp.sh`
- <https://github.com/lmc999/RegionRestrictionCheck> 是否解锁流媒体检测
- <https://github.com/P3TERX/warp.sh> 解锁流媒体脚本
- <https://bgp.he.net/> 原生IP查询，输入IP地址，Whois 查看 City，可以看到注册地址 （机房地址和IP注册地址一致就是原生IP）[linux 安装 whois （whois + ip）查询]
```
如果要解锁流媒体需要 ipv4 和 ipv6 都解锁，直接禁掉 ipv6，只需要保证 ipv4 解锁即可。

# 禁用ipv6
sysctl -w net.ipv6.conf.all.disable_ipv6=1; sysctl -w net.ipv6.conf.default.disable_ipv6=1
# 启用ipv6
sysctl -w net.ipv6.conf.all.disable_ipv6=0; sysctl -w net.ipv6.conf.default.disable_ipv6=0
# 重载配置使生效
sysctl --system 
```

## 去广告
- <https://github.com/Loyalsoldier/v2ray-rules-dat>
- <https://freevpn-x.com/index-101.htm> 
- <https://github.com/z44499783/NoADList>
- <https://github.com/uniartisan/adblock_list>
- <https://github.com/privacy-protection-tools/anti-AD>


```
https://easylist-downloads.adblockplus.org/easylist.txt
https://easylist-downloads.adblockplus.org/easylistchina.txt
https://raw.githubusercontent.com/uniartisan/adblock_list/master/adblock_plus.txt
https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-adguard.txt
http://sub.adtchrome.com/adt-chinalist-easylist360.txt
https://raw.githubusercontent.com/vokins/yhosts/master/hosts
```
# 机场 && 服务器 [所有机场都有跑路风险]
- https://sms-activate.org/cn 接码平台

* <https://www.kamatera.com/> VPS服务商（成立于1995）4$/Month
* <https://duocloud.net/clientarea.php?action=services> ipv6服务器
* <https://beibeilink.top/> 贝贝云(10/80GB)
* <https://nfcloud.net/> nfcloud（38/150GB）
* <https://fbweb01.flyingbird.one/> 飞鸟云（15/100GB) 通常有8折优惠
