import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

file_path = "images/traffic5.jpg"
im = cv2.imread(file_path)
bbox,label,conf = cv.detect_common_objects(im)
output_image = draw_bbox(im, bbox, label, conf)
plt.imshow(output_image)
plt.show()
pred = str(label.count('car') + label.count('bus') + label.count('motorcycle') + label.count('person') + label.count('truck') )
print(pred)
