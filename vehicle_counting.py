#----------------------------------------------
#--- Author         : Ahmet Ozlu
#--- Mail           : ahmetozlu93@gmail.com
#--- Date           : 27th January 2018
#----------------------------------------------

# Imports
# import tensorflow as tf

# # Object detection imports
# from utils import backbone
# from api import object_counting_api

# input_video = "./input_images_and_videos/vehicle_survaillance.mp4"

# # By default I use an "SSD with Mobilenet" model here. See the detection model zoo (https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md) for a list of other models that can be run out-of-the-box with varying speeds and accuracies.
# detection_graph, category_index = backbone.set_model('ssd_mobilenet_v1_coco_2018_01_28', 'mscoco_label_map.pbtxt')

# is_color_recognition_enabled = 1 # set it to 1 for enabling the color prediction for the detected objects
# roi = 185 # roi line position
# deviation = 2 # the constant that represents the object counting area

# object_counting_api.cumulative_object_counting_y_axis(input_video, detection_graph, category_index, is_color_recognition_enabled, roi, deviation) # counting all the objects


import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
im = cv2.imread("images/traffic4.jpg")
bbox, label, conf = cv.detect_common_objects(im)
output_image = draw_bbox(im, bbox, label, conf)
plt.imshow(output_image)
plt.show()
print('Number of Vehicles in the image is '+ str(label.count('car') + label.count('bus') + label.count('motorcycle') + label.count('person') + label.count('truck') ))
##adding person since it considers motobikes as 'person'