## YOLOv3 Object Detection:

YOLO is an algorithm that uses neural networks to provide real-time object detection.

## Object Detection by YOLO

In this project we aimed to report the performance of YOLO on COCO dataset. In COCO dataset there are approximately 81k training images and 41k validation images. Detailed descriptions can be found from the [COCO dataset's homepage](http://cocodataset.org/#home). 

YOLOv3-608 is used as the model to see how YOLO provides performance in training and validation images. We chose this model because if we look at other models of YOLO, we can observe that YOLOv3-608 is better than other models according to [homepage of YOLO](https://pjreddie.com/darknet/yolo/). We used darknet, which is the backbone of YOLO with python interpreter. Also we used OpenCV library with python interpreter. 

The steps of making the project can be divided into 3, which are:
* Getting ground truth (GT) information from COCO dataset and obtaining image names.
* Extraction of predictions which are made by YOLO for training and validation images. 
* Measuring performance of YOLO with reporting YOLO's predictions according to ground truth data.

### Adjusting the Ground Truth and Image Id Files

For arranging this files, We write [CocoAnnotations.py](YOLO/Setup/CocoAnnotations.py) script to generate necessary files. (The file can be downloaded with the link given. ) However, before using this code, you must set annotation files path and you must enter the annotation file name (train or val) by changing target variable.
You have to copy the training and validation info in json format to annotion directory. Currently we use COCO instances_train2014.json and instances_val2014.json file which can be downloaded from [here.](http://images.cocodataset.org/annotations/annotations_trainval2014.zip)

After adjusting python file you can run this script from terminal by writing

```
python CocoAnnotations.py
```

Python code will generate the following files. We've added descriptions of the files.

* [trainGT.txt](YOLO/Files/trainGt.txt) : Inside this file there are training image Id's, corresponding bounding boxes with class level information.

* [valGT.txt](YOLO/Files/valGt.txt) : Inside this file there are validaiton image Id's, corresponding bounding boxes with class level information.

* [trainImageIdForYolo.txt](YOLO/Files/trainImageIdForYolo.txt) : This file contains the name list of the COCO training dataset image.

* [valImageIdForYolo.txt](YOLO/Files/valImageIdForYolo.txt) : This file contains the name list of the COCO validation dataset image.

The links to these text files are set as an example in the YOLO directory.

### Running YOLO for Getting Predictions

You need to run [YoloPrediction.py](YOLO/Setup/YoloPrediction.py) to generate the prediction files (use image id txt files (trainImageIdForYolo.txt or valImageIdForYolo.txt) which are created in the previous step, don't forget to change paths to access to YOLO config file and YOLO weight file). After setting these variables you can run the code from terminal by writing

```
python3 YoloPrediction.py
```

This code generate the following files. We've added descriptions of the files.

* [predstrain.txt](YOLO/Files/predstrain.txt) : This file contains the predictions made by YOLO for training images.

* [predsval.txt](YOLO/Files/predsVal.txt) : This file contains the predictions made by YOLO for validation images.

The links are also given here, to set an example; can be found in the YOLO directory.

### Running Evaluation Tool For Obtaining YOLO Performance

Before running evaluation tool, we need to make following arrangements.

* Copy trainGT.txt file to trainlogs directory and change its name to gt.txt

* Copy predstrain.txt file to trainlogs directory and change its name to preds.txt

* Copy valGT.txt file to vallogs directory and change its name to gt.txt

* Copy predsval.txt file to vallogs directory and change its name to preds.txt

Switch to directory of [Evaluate_Models.ipynb](YOLO/Evaluation/Evaluate_Models.ipynb) file and write terminal to jupyter lab. Run Evaluate_Models.ipynb to generate performance results.
