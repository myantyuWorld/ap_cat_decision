import glob
import os
from flask import Flask, jsonify, request
import json
import base64
from io import BytesIO

app = Flask(__name__)

IMAGE_PATH = "\image\\*"

@app.route('/api/motion', methods=['POST'])
def save_picture():
    print(request.files)
    # file name
    fs = request.files['imageFile']
    # file save
    fs.save(os.getcwd() + '\image\\' + fs.filename)
    return "ok"

@app.route('/api/picture', methods=['GET'])
def get_picture(pictureId):
    return ""

@app.route('/api/pictures', methods=['GET'])
def get_pictures():

    fileList = []
    files = glob.glob(os.getcwd() + IMAGE_PATH)
    
    print(os.getcwd() + IMAGE_PATH)
    for f in files:
        with open(f, "rb") as img_file:
            img = {
                "filename" : f,
                "img" : base64.b64encode(img_file.read()).decode('utf-8')
            }
            fileList.append(img)

    return jsonify({"fileList" : fileList})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=5000)
