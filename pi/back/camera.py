#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from flask_cors import CORS
import numpy as np
import base64
import time
import picamera
import os
from datetime import datetime

import glob
from smb.SMBConnection import SMBConnection

app = Flask('flask-tesseract-api')
CORS(app)

def image_file_to_base64(file_path):
    with open(file_path, "rb") as image_file:
        data = base64.b64encode(image_file.read())

    return data.decode('utf-8')

@app.route('/')
def index():
    name = "Hello World"
    return name

@app.route('/image')
def get_image():
    return image_file_to_base64("./sample/25.png")

@app.route('/images')
def get_images():
    data = []

    files =glob.glob("/home/pi/ap_cat_decision/*.jpg")
    print(files)

    for fname in files:
        print(fname)
        with open(fname, "rb") as image_file:
            image_data = base64.b64encode(image_file.read())
            
        obj = {
            "file_name" : fname,
            "base64" : image_data
        }
        data.append(obj)

    return jsonify(data)

@app.route('/shooting')
def shooting():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_preview()
        time.sleep(2)
        timestr = datetime.now().strftime('%Y%m%d%H%M%S')
        camera.capture(timestr +'.jpg')

    return image_file_to_base64(timestr + '.jpg')

@app.route('/good')
def good():
    name = "Good"
    return name

## おまじない
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
