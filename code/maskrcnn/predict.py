import cv2
import detectron2
from detectron2.utils.logger import setup_logger

import numpy as np
import os, json, cv2, random
# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.data.datasets.coco import load_coco_json

setup_logger()
im = cv2.imread("/home/lu/detectron2/yanzheng/tile_13_0.jpg")
cfg = get_cfg()#获取默认的配置参数
# add project-specific config (e.g., TensorMask) here if you're not running a model in detectron2's core library
cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
# Find a model from detectron2's model zoo. You can use the https://dl.fbaipublicfiles... url as well
cfg.MODEL.WEIGHTS = ("/home/lu/detectron2/output/model_final.pth")


predictor = DefaultPredictor(cfg)
outputs = predictor(im)
print(outputs["instances"].pred_classes)
print(outputs["instances"].pred_boxes)

####

#声明类别，尽量保持
CLASS_NAMES =["potato","weed"]
# 数据集路径
DATASET_ROOT = '/home/lu/detectron2/potato'
ANN_ROOT = os.path.join(DATASET_ROOT, 'COCOformat')

TRAIN_PATH = os.path.join(DATASET_ROOT, 'JPEGImages')
VAL_PATH = os.path.join(DATASET_ROOT, 'JPEGImages')

TRAIN_JSON = os.path.join(ANN_ROOT, 'train.json')
VAL_JSON = os.path.join(ANN_ROOT, 'val.json')
#VAL_JSON = os.path.join(ANN_ROOT, 'test.json')

# 声明数据集的子集
PREDEFINED_SPLITS_DATASET = {
    "coco_my_train": (TRAIN_PATH, TRAIN_JSON),
    "coco_my_val": (VAL_PATH, VAL_JSON),
}
#===========以下有两种注册数据集的方法，本人直接用的第二个plain_register_dataset的方式 也可以用register_dataset的形式==================
#注册数据集（这一步就是将自定义数据集注册进Detectron2）

#=============================
# 注册数据集和元数据

    #训练集
DatasetCatalog.register("coco_my_train", lambda: load_coco_json(TRAIN_JSON, TRAIN_PATH))
MetadataCatalog.get("coco_my_train").set(thing_classes=CLASS_NAMES,  # 可以选择开启，但是不能显示中文，这里需要注意，中文的话最好关闭
                                                    evaluator_type='coco', # 指定评估方式
                                                    json_file=TRAIN_JSON,
                                                    image_root=TRAIN_PATH)

    #DatasetCatalog.register("coco_my_val", lambda: load_coco_json(VAL_JSON, VAL_PATH, "coco_2017_val"))
    #验证/测试集
DatasetCatalog.register("coco_my_val", lambda: load_coco_json(VAL_JSON, VAL_PATH))
MetadataCatalog.get("coco_my_val").set(thing_classes=CLASS_NAMES, # 可以选择开启，但是不能显示中文，这里需要注意，中文的话最好关闭
                                                evaluator_type='coco', # 指定评估方式
                                                json_file=VAL_JSON,
                                                image_root=VAL_PATH)
###
#v = Visualizer(im[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2)
v = Visualizer(im[:, :, ::-1], MetadataCatalog.get("coco_my_val"), scale=1.2)
out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
cv2.imwrite("b.jpg", out.get_image()[:, :, ::-1])