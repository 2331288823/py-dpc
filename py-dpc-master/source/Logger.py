import logging


def logger_config(log_path, logging_name):
    """
    配置log
    :param log_path: 输出log路径
    :param logging_name: 记录中name，可随意
    :return:
    """
    '''
    logger是日志对象，handler是流处理器，console是控制台输出（没有console也可以，将不会在控制台输出，会在日志文件中输出）
    '''
    """
    代码来源：https://blog.csdn.net/qq_36187544/article/details/100893525
    """
    # 获取logger对象,取名
    logger_name = logging.getLogger(logging_name)
    # 输出DEBUG及以上级别的信息，针对所有输出的第一层过滤
    logger_name.setLevel(level=logging.DEBUG)
    # 获取文件日志句柄并设置日志级别，第二层过滤
    handler = logging.FileHandler(log_path, encoding='UTF-8')
    handler.setLevel(logging.INFO)
    # 生成并设置文件日志格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # console相当于控制台输出，handler文件输出。获取流句柄并设置日志级别，第二层过滤
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    # 为logger对象添加句柄
    logger_name.addHandler(handler)
    logger_name.addHandler(console)
    return logger_name
