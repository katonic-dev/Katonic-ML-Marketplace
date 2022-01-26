### This routin is written by Mustafa Bunyamin Sagman, January 2019 ###
### If you have any problem just send an e-mail to mbunyamins@gmail.com ###

# from darknet.detector import Detector, Image

import urllib
import urllib.request
import cv2
import time
import numpy as np
import os
import matplotlib.pyplot as plt
# from darknet.darknet import Darknet, Image
from pydarknet import Detector, Image

names = open(("/home/katonic/Deep-Performance-Evaluation-Tool/YOLO/Setup/data/coco.names"),'r')
lineName = names.read().split("\n")

# cfg_file = './cfg/yolov3.cfg'
# weight_file = './yolov3.weights'

# net = Darknet(cfg_file)
# net.load_weights(weight_file)


net = Detector(bytes("./yolov3.cfg", encoding="utf-8"), bytes("./yolov3.weights", encoding="utf-8"), 0, bytes("./coco.data",encoding="utf-8"))
start_time = time.time()

#path = "/home/mspr/darknet/coco/train2014/"
path = "/home/katonic/Deep-Performance-Evaluation-Tool/"
dosya = open(("/home/katonic/Deep-Performance-Evaluation-Tool/results.txt"),'w')
ForRutin = open (("/home/katonic/Deep-Performance-Evaluation-Tool//PredsWithIDs.txt"),'w')

infile = open("/home/katonic/Deep-Performance-Evaluation-Tool/YOLO/Files/valImageIdForYolo.txt","r")
#infile = open("/home/sagman/darknet/coco/imageIdForTrain.txt","r")
lines = infile.read().split("\n")
#dosya = open(("/home/mspr/darknet/coco" + "/results.txt"),'w')
Files = os.listdir(path)
string1 = path + "results"
if not os.path.exists(string1):
	os.makedirs(string1)
class_id = 0
for i,line in enumerate(lines):
    image_path = 'http://images.cocodataset.org/val2014/'
    image_url = image_path + "COCO_val2014_" + str(line) + ".jpg"
    print('image_url', image_url)
    resp = urllib.request.urlopen(image_url)
    image_name = np.asarray(bytearray(resp.read()), dtype="uint8")
    img = cv2.imdecode(image_name, cv2.IMREAD_COLOR)
    #imagename = "COCO_train2014_" + str(line) + ".jpg"
#     print(imagename)
#     img = cv2.imread(imagename)
    img_darknet = Image(img)
    results = net.detect(img_darknet, thresh = 0.5)
    print(results)

    for cat, score, bounds in results:

        x, y, w, h = bounds
        classes1 = cat # .decode("utf-8")
        #classes1 = classes1 + "/n"
        #print(classes1)

        for name in lineName:
            liste = name.split(",")
#             print('name:', name)            
#             print('liste:', liste)

            if(str(liste[1]) == str(classes1)):
                print (liste[1])
                print(liste[0])
                class_id = int(liste[0])
        xmin = x - w/2
        xmin = round(xmin)
        ymin = y - h/2
        ymin = round(ymin)
        xmax = x + w/2
        xmax = round(xmax)
        ymax = y + h/2
        ymax = round(ymax)

        cv2.rectangle(img, (int(x - w / 2), int(y - h / 2)), (int(x + w / 2), int(y + h / 2)), (255, 0, 0), thickness=2)
        cv2.putText(img,str(cat),(int(x),int(y)),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0))
        dosya.write(str(line) + "," + str(class_id) + ",[" + str(ymin) + " " + str(xmin) + " " + str(ymax) + " " + str(xmax) + "]" + "\n")
        ForRutin.write(str(i) + "," + str(class_id) + ",[" + str(ymin) + " " + str(xmin) + " " + str(ymax) + " " + str(xmax) + "]" + "\n")
    string = str(string1) + "/" + str(line) + ".jpg"
    #print (string)
    cv2.imwrite(string, img)

ForRutin.close()
dosya.close()

