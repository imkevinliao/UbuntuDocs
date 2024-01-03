
# Linux 读写权限
rwx: 读 写 执行 （4,2,1) (2^2,2^1,2^0)

ugo: 用户 群组 其他 （user group other）

755 = 用户拥有读写执行 群组和其他人拥有读加执行 7=4+2+1 5=4+1

# 列出所有由人创建的用户：
command1: cut -d: -f1,3 /etc/passwd | egrep ':[0-9]{4}$' | cut -d: -f1

command2: awk -F: '$3 >= 1000 && $1 != "nobody" {print $1}' /etc/passwd   

# 删除最新的解压文件
tar -tf <file.tar.gz> | parallel rm

[参考链接](https://www.commandlinefu.com/commands/view/2573/remove-all-files-previously-extracted-from-a-tar.gz-file)
