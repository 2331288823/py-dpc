import os
import sys
import platform


def clear_screen():
    if sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('win'):
        os.system('cls')


def menu_display(menu_list: list) -> int:
    """
    显示菜单，并返回选择的值
    输入：菜单名称列表
    输出：打印整个菜单
    返回：选择的数字
    """
    while True:
        num = 0
        for item in menu_list:
            num += 1
            print(f"{num}.{item}")
        print("0.退出")

        try:
            choice_str = input("请输入序号：")
            choice_num = int(choice_str)
        except KeyboardInterrupt:
            os.system("cls")
            print("程序结束\n")
            return 0
        except ValueError:
            print("输入数字不为整数，请重新输入")
        else:
            return choice_num
