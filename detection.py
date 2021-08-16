# Author: Swati Sinha & Maitry Sinha
# Date : 13-08-2021

import cv2
import numpy as np
import pybase64

weight_path = 'frozenGraph.pb'
config_path = 'SSDmobilenet_coco.pbtxt'
## Defined for coco class names
class_names = []


class SSDmobileNet:
    def __init__(self, weight_path=weight_path, config_path=config_path, class_names=class_names):
        self.weight_path = weight_path
        self.config_path = config_path
        self.class_names = class_names


    # compiling detection model architecture and returning required network
    def network(self):
        net = cv2.dnn_DetectionModel(self.weight_path, self.config_path)
        net.setInputSize(320, 320)
        net.setInputScale(1.0 / 127.5)
        net.setInputMean((127.5, 127.5, 127.5))
        net.setInputSwapRB(True)
        return net

    ## returning required class names
    def classNames(self):
        if len(self.class_names) == 0:
            classFile = 'coco.names'
            with open(classFile, 'rt') as f:
                classNms = f.read().rstrip('\n').split('\n')
            labels = ['background'] + classNms  ## given background as zero class name
        else:
            labels = self.class_names  ## for custom class names
        return labels



def Decode(image):
    imgdata = pybase64.b64decode(image)
    image1 = np.asarray(bytearray(imgdata), dtype="uint8")
    image1 = cv2.imdecode(image1, cv2.IMREAD_COLOR)
    return image1


## making bounding boxes, drawing boxes, making prediction, returning class text
def predict(net, labels, img, cthres=0.35, nthres=0.3):
    classIds, conf, bbox = net.detect(img, confThreshold=cthres)
    bbox = list(bbox)
    conf = list(np.array(conf.reshape(1, -1)[0]))
    conf = list(map(float, conf))
    # making Non Maximize Suppression for removing unwanted boxes
    indices = cv2.dnn.NMSBoxes(bbox, conf, cthres, nms_threshold=nthres)
    for i in indices:
        i = i[0]
        box = bbox[i]
        ## getting initial co-ordinate width and height of each boxes
        x, y, w, h = box[0], box[1], box[2], box[3]
        cv2.rectangle(img, (x, y), (x + w, y + h), color=(0, 255, 255), thickness=2)
        text = labels[classIds[i][0]]
        # filtering required classes of vehicles from coco classes
        # for 'bicycle', 'car', 'motorbike', 'aeroplane', 'bus', 'train', 'truck', 'boat'
        if text in labels[2:10]:
            cv2.rectangle(img, (x, y), (x + 140, y - 24), (0, 255, 255), cv2.FILLED)
            cv2.putText(img, text.upper(), (x + 2, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
            ## saving predicted image output
            cv2.imwrite('static/output.jpg', img)
            return text
        else:
            pass
