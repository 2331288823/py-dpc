"""
与数学相关的各种函数
"""
# 设置计算斐波拉契需要的全局字典
fibonacci_dic = {1: 1, 2: 1}


def get_fibonacci(n: int) -> int:
    """
    获取斐波拉契数
    """
    if fibonacci_dic.get(n):
        return fibonacci_dic.get(n)
    else:
        result = get_fibonacci(n - 1) + get_fibonacci(n-2)
        fibonacci_dic[n] = result  # 更新字典
        return result


def fibonacci_sequence(n: int) -> list:
    """
    获取斐波拉契数列
    """
    fibonacci_list = []
    for i in range(1, n+1):
        fibonacci_list.append(get_fibonacci(i))
    return fibonacci_list
