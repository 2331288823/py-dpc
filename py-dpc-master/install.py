import shutil
import os
import sys

# 获取当前用户目录
user_home = os.path.expanduser('~')

# 文件夹位置
source_path = "./source"
# 在不同系统下，使用不同路径
target_path = ""
if sys.platform.startswith('win'):
    # 获取Python版本
    pythonVersion = str(sys.version_info[0]) + str(sys.version_info[1])
    target_path = user_home + '/AppData/Local/Programs/Python/Python' + pythonVersion + '/Lib/site-packages/pyDPC'
elif sys.platform.startswith('linux'):
    # 获取Python版本
    pythonVersion = str(sys.version_info[0]) + '.' + str(sys.version_info[1])
    target_path = "/data/data/com.termux/files/usr/lib/python" + pythonVersion + "/site-packages/pyDPC"


def info_display():
    print(f"Python版本信息：{pythonVersion}")
    print(f"安装位置：{target_path}")


def copy_folder(from_dir_path, to_dir_path):
    if os.path.exists(to_dir_path):
        print("正在卸载pyDPC")
        shutil.rmtree(to_dir_path)
    print("正在安装pyDPC")
    shutil.copytree(from_dir_path, to_dir_path)
    print("安装成功")


if __name__ == "__main__":
    info_display()
    copy_folder(source_path, target_path)
