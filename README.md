# YOLO5-Inference #
Inference using the YOLOv5 object detection model
You Only Look Once (YOLO) algorithm combines classification and bounding box prediction into a single neural network.
YOLO examines the entire image in one pass, capturing the contextual information of detected objects, thus reducing false-positive detections compared to methods that analyze different image regions separately, while preserving generalization capabilities.
This approach known as the **Single Shot Detector**: where object detection and classification are performed in a single pass through the network.

**You Only Look Once (V1)**:
```
bibtex
@inproceedings{redmon2016you,
  title={You only look once: Unified, real-time object detection},
  author={Redmon, Joseph and Divvala, Santosh and Girshick, Ross and Farhadi, Ali},
  booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
  pages={779--788},
  year={2016}
}
```

**YOLOv5** is a an object detection model introduced by Ultralytics.
For more information about [YOLOv5](https://github.com/ultralytics/yolov5), you can refer to the official Ultralytics repository: 

<p align="center">
<img src="https://miro.medium.com/v2/resize:fit:1152/1*m8p5lhWdFDdapEFa2zUtIA.jpeg" width="500" height="500">
</p>

**Required Libraries:**
```
pip install -r requirements.txt
```
from venv:
```
# Create a virtual environment
python3 -m venv <venvname>
# Activate the virtual environment
.\<venvname>\Scripts\activate
pip install -r requirements.txt
```
**Usage**

1.Clone this repository or download the script file.

2.Install the dependencies mentioned in the prerequisites section.

3.Run the script using the following command:

```
python ./detector_yolo5.py
```

When prompted, enter the link for the the jpeg image:
```
Enter the path of the image: <PATH_TO_YOUR_JPEG_FILE>
```
