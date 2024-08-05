import importlib.util
import os

def config_to_dict(file_path):
    # 获取模块名和文件路径
    module_name = os.path.splitext(os.path.basename(file_path))[0]
    
    # 动态导入模块
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # 提取全局变量
    config_dict = dict()
    for k, v in vars(module).items():
        if k.startswith('__') or v is None:
            continue
        config_dict[k] = v

    return config_dict

from datetime import datetime

def get_formatted_time():
    """
    获取当前时间并格式化为 'YYYY-MM-DD' 格式

    返回:
    str: 格式化后的时间字符串
    """
    # 获取当前时间
    current_time = datetime.now()

    # 格式化时间
    formatted_time = current_time.strftime('%Y-%m-%d')

    return formatted_time

def generate_name(naive_name=None):
    """
    生成格式化时间和6位序列号组成的名字

    返回:
    str: 生成的名字
    """
    current_time = datetime.now()
    formatted_time = current_time.strftime('%Y-%m-%d')
    sequence_number = current_time.strftime('%H%M%S%f')[:6]  # 使用当前时间的秒和微秒生成6位序列号
    name = f"{formatted_time}-{sequence_number}"
    if naive_name is None:
        return name
    else:
        return naive_name + '-' + name

def f1_score(precision, recall):
    # 计算F1分数
    f1_score = 2 * (precision * recall) / (precision + recall)
    return f1_score

if __name__ == '__main__':
    # from objprint import op
    # file_path = 'SARs/default_training_setting.py'
    # config_dict = config_to_dict(file_path)
    # op(config_dict)

    print(generate_name())