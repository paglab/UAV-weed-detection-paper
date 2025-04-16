import os
import json
import glob
import cv2
import numpy as np
import matplotlib.pyplot as plt


def labelme_json_to_yolo_seg_format(input_json_dir, output_text_dir):
    # transfer labelme json to yolo txt label  (only for segmentation)
    jsons = glob.glob(os.path.join(input_json_dir, "*.json"))
    for item in jsons:
        with open(item) as fb:
            data = json.load(fb)
            shapes = data['shapes']
            height = data['imageHeight']
            width = data['imageWidth']
            image_path = data['imagePath']
            basename = os.path.basename(image_path).split('.')[0]
            output_txt = os.path.join(output_text_dir, basename + '.txt')
            with open(output_txt, 'w') as fb2:
                for shape in shapes:
                    shape_type = shape['shape_type']
                    points = shape['points']
                    label = shape['label']
                    points = np.array(points)
                    if shape_type == 'polygon':
                        x = points[:, 0] / width
                        y = points[:, 1] / height
                        xyxy = [str(x) for pair in zip(x, y) for x in pair]
                        xyxy = ' '.join(xyxy)
                        line = '{} {}'.format(label, xyxy)
                        fb2.write(line)
                        fb2.write('\n')
            print("output={}, done".format(output_txt))


def show_yolo_txt_image(txt_path, image_path, image_fmt='.png'):
    # show labeled image  from yolo txt
    label_txt = glob.glob(os.path.join(txt_path, "*.txt"))
    images = glob.glob(os.path.join(image_path, "*{}".format(image_fmt)))
    for item in label_txt:
        txt_basename = os.path.basename(item).split('.')[0]
        for image in images:
            img = cv2.imread(image)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w = img.shape[:2]
            img_basename = os.path.basename(image).split('.')[0]
            if img_basename == txt_basename:
                with open(item) as fb:
                    lines = fb.readlines()
                    for line in lines:
                        labeled = line.split(' ')
                        cls = labeled[0]
                        xyxy = labeled[1:]
                        x = xyxy[::2]
                        y = xyxy[1::2]
                        x = np.array(x, dtype=np.float)
                        y = np.array(y, dtype=np.float)
                        x2 = x * w
                        y2 = y * h
                        lst = list(zip(x2, y2))
                        points = np.array(lst, dtype=np.int32)
                        cv2.polylines(img, [points], isClosed=True, color=(0, 0, 255), thickness=5)
                    plt.imshow(img)
                    plt.show()


if __name__ == "__main__":
    input_ = r'C:\Users\38492\ultralytics\potato_new_binary\labels\train'
    output = r'C:\Users\38492\ultralytics\potato_new_binary\labels\train'
    labelme_json_to_yolo_seg_format(input_, output)
    #show_yolo_txt_image(output, input_)
