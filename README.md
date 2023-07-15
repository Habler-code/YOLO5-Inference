# YOLO5-Inference #
Inference using the YOLOv5 object detection model
You Only Look Once (YOLO) algorithm combines classification and bounding box prediction into a single neural network.
YOLO examines the entire image in one pass, capturing the contextual information of detected objects, thus reducing false-positive detections compared to methods that analyze different image regions separately, while preserving generalization capabilities.
This approach known as the **Single Shot Detector**: where object detection and classification are performed in a single pass through the network.

**YOLOv5** is a an object detection model introduced by Ultralytics.
For more information about [YOLOv5](https://github.com/ultralytics/yolov5), you can refer to the official Ultralytics repository: 

![YOLO]([https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.section.io%2Fengineering-education%2Fintroduction-to-yolo-algorithm-for-object-detection%2Fhow-yolo-algorithm-works.jpg&tbnid=pmw1V910NcZ6iM&vet=12ahUKEwjfqvqLzJCAAxWLmScCHWdmCrMQMygDegUIARDJAQ..i&imgrefurl=https%3A%2F%2Fwww.section.io%2Fengineering-education%2Fintroduction-to-yolo-algorithm-for-object-detection%2F&docid=fxZV8qcXMl2-rM&w=483&h=324&q=what%20is%20yolo%20&ved=2ahUKEwjfqvqLzJCAAxWLmScCHWdmCrMQMygDegUIARDJAQ](https://miro.medium.com/v2/resize:fit:1152/1*m8p5lhWdFDdapEFa2zUtIA.jpeg))


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
