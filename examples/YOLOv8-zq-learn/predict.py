#%%
import os
import ultralytics
from ultralytics import YOLO
from loguru import logger

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(BASE_DIR))
EXAMPLES = os.path.join(ROOT, "examples")
WEIGHTS = os.path.join(ROOT, "weights")
#%%
logger.info(f'{ultralytics.__version__=}')

#%%
model = YOLO("yolov8n.yaml")
model.load(os.path.join(WEIGHTS, "yolov8n.pt"))
img_fnames = ['bus.jpg', 'zidane.jpg']
imgs = [os.path.join(EXAMPLES, fname) for fname in img_fnames]
results = model(imgs)
for result in results:
    result.show()
# %%
