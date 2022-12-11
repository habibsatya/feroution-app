import torch
import numpy as np
import cv2

model1 = torch.hub.load("yolo", 'custom', path="best.pt", source='local')

img = cv2.imread('yolo/photos/cobakomedo3.jpg')

results = model1(img)
new_results = np.array(results.pandas().xyxy[0])

print(new_results[0][5])
