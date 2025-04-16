<<<<<<< HEAD
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 加载预训练的 YOLOv8n 模型
model = YOLO(r'C:\Users\38492\ultralytics\runs\segment\train_refine\weights\best.pt')

# 定义图像文件的路径
source = r'C:\Users\38492\ultralytics\potato\images\val\tile_14_6.jpg'

# 对来源进行推理
results = model(source,save=True,save_txt=True,show_labels=True,show_conf=True,
                #classes=1,
                imgsz=[640,640])  # Results 对象列表


=======
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 加载预训练的 YOLOv8n 模型
model = YOLO(r'C:\Users\38492\ultralytics\runs\segment\train_refine\weights\best.pt')

# 定义图像文件的路径
source = r'C:\Users\38492\ultralytics\potato\images\val\tile_14_6.jpg'

# 对来源进行推理
results = model(source,save=True,save_txt=True,show_labels=True,show_conf=True,
                #classes=1,
                imgsz=[640,640])  # Results 对象列表


>>>>>>> 94c54e4f848ace37bf7c1afad41b08a90af25c23
