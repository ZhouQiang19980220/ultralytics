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

if __name__ == '__main__':
    from objprint import op
    file_path = 'SARs/default_training_setting.py'
    config_dict = config_to_dict(file_path)
    op(config_dict)