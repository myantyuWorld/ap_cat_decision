from flask import Flask, jsonify, request
import json
import base64

app = Flask(__name__)

@app.route('/api/motion', methods=['POST'])
def hello():
    return "aaa"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=5000)
