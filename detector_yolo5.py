import torch
import cv2
from matplotlib import pyplot as plt

# Define the main function
def main(image_path):
    print(f'image path is: {image_path}')

    # Download a pretrained model
    print("Downloading a Pre-Trained Model of YOLO V5")
    torch.hub.download_url_to_file('https://github.com/ultralytics/yolov5/releases/download/v5.0/yolov5s.pt', 'yolov5s.pt')

    print("Running inference")
    model = torch.hub.load('ultralytics/yolov5', 'custom', 'yolov5s.pt')
    results = model(image_path)
    results.show()

    print("Loading Pre-Trained Model")
    model_local = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=False)

    # Predict the image
    print("Predicting the image...")
    prediction = model_local(image_path)

    # Show the prediction
    print("Showing the prediction...")
    model_local.show(image_path)

# Call the main function
if __name__ == "__main__":
    image_path = input("Enter the path of the image: ")
    main(image_path)
