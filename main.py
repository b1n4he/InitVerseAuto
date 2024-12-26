import os

# 安装pm2
def install_environment():
    c1 = "wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash"
    c2 = '''
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
'''
    c3 = "sudo npm install pm2 -g -y"
    os.system(c1)
    os.system(c2)
    os.system(c3)


def install_node():
    # 从用户输入获取钱包和机器名称
    wallet = input("请输入钱包地址：")
    name = input("请输入机器名称（默认为work01）：")
    if not name:
        name = "work01"

    c1 = "wget https://github.com/Project-InitVerse/miner/releases/download/v1.0.0/iniminer-linux-x64"
    c2 = "chmod a+x iniminer-linux-x64"
    # 这里默认使用全部cpu，如果需要指定cpu数量，可以修改下面的命令，增加--cpu-devices
    c3 = f'pm2 start iniminer-linux-x64 --name="initverse" -- --pool stratum+tcp://{wallet}.{name}@pool-core-testnet.inichain.com:32672'
    os.system(c1)
    os.system(c2)
    os.system(c3)



def view_node_logs():
    c1 = "pm2 log initverse"
    os.system(c1)


def stop_node():
    c1 = "pm2 stop initverse"
    os.system(c1)


def main():
    print("欢迎使用节点管理脚本！")
    print("请选择操作：")
    print("1. 安装环境")
    print("2. 安装节点")
    print("3. 查看节点日志")
    print("4. 停止节点")
    print("5. 退出脚本")

    choice = input("请输入选项数字：")

    if choice == "1":
        install_environment()
    elif choice == "2":
        install_node()
    elif choice == "3":
        view_node_logs()
    elif choice == "4":
        stop_node()
    elif choice == "5":
        exit(0)
    else:
        print("无效的选择。")





if __name__ == "__main__":
    while True:
        try:
            main()
        except SystemExit:
            break
        except:
            # 捕获其他所有异常，并打印错误消息
            print("[x] 出现错误，无法继续运行")
