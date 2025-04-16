<<<<<<< HEAD
from ultralytics import YOLO
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
# 载入一个模型
model = YOLO('yolov8n-seg.yaml')  # 从YAML构建一个新模型
model = YOLO('yolov8n-seg.pt')  # 载入预训练模型（推荐用于训练）
model = YOLO('yolov8n-seg.yaml').load('yolov8n.pt')  # 从YAML构建并传递权重

# 训练模型
if __name__ == '__main__':
=======
from ultralytics import YOLO
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
# 载入一个模型
model = YOLO('yolov8n-seg.yaml')  # 从YAML构建一个新模型
model = YOLO('yolov8n-seg.pt')  # 载入预训练模型（推荐用于训练）
model = YOLO('yolov8n-seg.yaml').load('yolov8n.pt')  # 从YAML构建并传递权重

# 训练模型
if __name__ == '__main__':
>>>>>>> 94c54e4f848ace37bf7c1afad41b08a90af25c23
    results = model.train(data='coco128-seg.yaml', epochs=400, imgsz=640)