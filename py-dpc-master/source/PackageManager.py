import os


def upgrade_package():
    # 更新所有包
    print("更新包中……")
    try:
        os.system("pipupgrade --latest")
    except ModuleNotFoundError as e:
        # 安装不存在的模块
        os.system("pip install " + e.name)
        # 再次尝试更新
        os.system("pipupgrade --latest")
    finally:
        print("更新完成")
        print("")

    # 生成requirements.txt
    print("生成requirements.txt中……")
    os.system("pipreqs . --encoding=utf-8 --force")
    print("生成requirements.txt完成")
