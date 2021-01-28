from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
from typing import Counter
import numpy as np

# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

# CVLib  Vehicle Detection
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

counter = 0

print('Model loaded. Check http://127.0.0.1:5000/ or http://localhost:5000/')

def clear_file():
    global counter
    counter = 1
    f = open('image-recognition-flask/Vehicle_count.txt', 'r+')
    f.truncate(0) # need '0' when using r+

def save_to_file(count):
    f = open('image-recognition-flask/Vehicle_count.txt', 'a+')
    f.write(count)
    f.write(" ")
    f.close()

def model_predict(file_path):
    global counter 
    counter +=1
    #im = image.load_img(img_path)
    img = cv2.imread(file_path)
    bbox,label,conf = cv.detect_common_objects(img)
    #output_image = draw_bbox(im, bbox, label, conf)

    preds = (str(label.count('car') + label.count('bus') + label.count('motorcycle') + label.count('person') + label.count('truck')))
    if counter == 5:
        clear_file()
    save_to_file(preds)
    return preds

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path)
        
        # Process your result for human
        # pred_class = preds.argmax(axis=-1)            # Simple argmax
        #pred_class = decode_predictions(preds, top=1)   # ImageNet Decode
                      # Convert to string       
        return preds
        
    return None


if __name__ == '__main__':
    # app.run(port=5002, debug=True)

    # Serve the app with gevent
    #http_server = WSGIServer(('', 5000), app)
    #http_server.serve_forever()
    app.run()

