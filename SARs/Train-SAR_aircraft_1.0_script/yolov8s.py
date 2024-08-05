#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
sys.path.append('/root/ultralytics/SARs')

import ultralytics
from ultralytics import YOLO
from utils import config_to_dict, generate_name
ultralytics.checks()


# In[ ]:


# 导入默认训练设置
default_config_dict = config_to_dict('/root/ultralytics/SARs/default_training_setting.py')

# frequently modify
config_dict = dict(
    epochs = 500,              
    batch = -1, 
    cache = True, 
    project = "YOLOv8s-train", 
    name = generate_name("train"),   # YYYY-mm-dd-ssssss
    pretrained = False, 
    close_mosaic = 30, 
    fraction = 1.0,             
    warmup_epochs = 9.0, 
    plots = True, 
)
default_config_dict.update(config_dict)
config_dict = default_config_dict

# build a model from scratch
model = YOLO('yolov8s.yaml')

# train the model on the “SAR aircraft 1.0” dataset

# train setting
# https://docs.ultralytics.com/modes/train/#train-settings
data_dir = "datasets/SAR-AIRcraft-1.0-yolo/SAR-AIRcraft-1.0-yolo/SARAIRcraft1.0.yaml"
model.train(
    data=data_dir, 
    **config_dict
) 

