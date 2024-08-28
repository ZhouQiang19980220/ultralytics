#%%
import os
import ultralytics
from ultralytics import YOLO
from ultralytics import utils
from loguru import logger

#%%
logger.info(f'{ultralytics.__version__=}')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(BASE_DIR))

#%% load model
model = YOLO(os.path.join(ROOT, "weights", "yolov8n.pt"))
#%%
results = model.train(
    data="coco8.yaml", 
    epochs=100, 
    imgsz=640, 
    project="coco8",
    name='yolov8n')


# %%
